using System;
using System.IO;
using System.Net;
using System.Net.Http;
using System.Text;
using System.Net.Sockets;
using System.Threading.Tasks;

class ProxyServer
{
    static async Task Main()
    {
        TcpListener tcpListener = new TcpListener(IPAddress.Any, 8080);
        tcpListener.Start();
        Console.WriteLine("Servidor proxy iniciado en el puerto 8080");

        while (true)
        {
            try
            {
                TcpClient client = await tcpListener.AcceptTcpClientAsync();
                HandleClient(client);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }

    static async void HandleClient(TcpClient client)
    {
        try
        {
            using (NetworkStream clientStream = client.GetStream())
            {
                byte[] buffer = new byte[5];
                int bytesRead = await clientStream.ReadAsync(buffer, 0, buffer.Length);
                string clientData = Encoding.ASCII.GetString(buffer, 0, bytesRead);

                if (clientData.StartsWith("CONNECT", StringComparison.OrdinalIgnoreCase))
                {
                    // Aquí puedes manejar solicitudes HTTPS si es necesario en el futuro
                }
                else
                {
                    await HandleHttpRequest(clientStream, clientData);
                }
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
        finally
        {
            client.Close();
        }
    }

    static async Task HandleHttpRequest(NetworkStream clientStream, string request)
    {
        try
        {
            // Analiza la solicitud HTTP
            string[] requestLines = request.Split(' ');
            string targetUrl = requestLines[1];

            using (HttpClient httpClient = new HttpClient())
            {
                HttpResponseMessage response = await httpClient.GetAsync(targetUrl);
                byte[] responseData = await response.Content.ReadAsByteArrayAsync();
                await clientStream.WriteAsync(responseData, 0, responseData.Length);
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error en HandleHttpRequest: {ex.Message}");
        }
    }
}