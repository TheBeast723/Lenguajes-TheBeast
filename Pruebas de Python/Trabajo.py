import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, StringVar
import csv
import os

class Producto:
    def __init__(self, nombre, cantidad, precio, talle):
        self.nombre = nombre
        self.talle = talle
        self.cantidad = cantidad
        self.precio = precio
        self.check = False
        self.checkbox_state = tk.BooleanVar()

class ControlDeStockApp:
    def __init__(self, root):
        self.productos = []
        self.archivo_csv = "productos.csv"

        # Crear el archivo CSV si no existe
        self.crear_archivo_csv_si_no_existe()

        # Configuración de la ventana principal
        root.title("Control de Stock App")
        root.geometry("630x530")

        # Crear y configurar widgets
        self.create_widgets()

        # Load saved data from CSV and display it
        self.cargar_datos_desde_csv()
        self.mostrar_prendas_en_grilla()

    def create_widgets(self):
        self.lblNombrePrenda = ttk.Label(root, text="Prenda:")
        self.lblTallePrenda = ttk.Label(root, text="Talle:")
        self.lblCantidad = ttk.Label(root, text="Cantidad:")
        self.lblPrecio = ttk.Label(root, text="Precio:")

        self.lblNombre = ttk.Label(root, text="Prenda")
        self.lblTalle = ttk.Label(root, text="Talle")
        self.lblCantidades = ttk.Label(root, text="Cantidad")
        self.lblPrecios = ttk.Label(root, text="Precio")
        self.lblVendida = ttk.Label (root, text= "Vendida")

        self.lblNombre2 = ttk.Label(root, text="Prenda")
        self.lblTalle2 = ttk.Label(root, text="Talle")
        self.lblCantidades2 = ttk.Label(root, text="Cantidad")
        self.lblPrecios2 = ttk.Label(root, text="Precio")
        self.lblVendida2 = ttk.Label (root, text= "Vendida")

        self.lblNombre3 = ttk.Label(root, text="Prenda")
        self.lblTalle3 = ttk.Label(root, text="Talle")
        self.lblCantidades3 = ttk.Label(root, text="Cantidad")
        self.lblPrecios3 = ttk.Label(root, text="Precio")
        self.lblVendida3 = ttk.Label (root, text= "Vendida")

        self.txtNombrePrenda = ttk.Entry(root)
        self.txtTallePrenda = ttk.Entry(root)
        self.txtCantidad = ttk.Entry(root)
        self.txtPrecio = ttk.Entry(root)

        self.btnAgregarPrenda = ttk.Button(root, text="Agregar Prenda", command=self.agregar_prenda)
        self.btnGuardar = ttk.Button(root, text="Guardar", command=self.guardar_prendas_en_csv)
        self.btnEditarPrenda = ttk.Button(root, text="Editar Prenda", command=self.editar_prenda_dialogo)
        self.btnEliminarPrenda = ttk.Button(root, text="Eliminar Prenda", command=self.eliminar_prenda)

        self.etiquetas_prendas = []  

        self.lblNombrePrenda.place(x=10, y=10)
        self.lblTallePrenda.place(x=10, y=40)
        self.lblCantidad.place(x=10, y=70)
        self.lblPrecio.place(x=10, y=100)

        self.lblNombre.place(x=10, y=130)
        self.lblTalle.place(x=150, y=130)
        self.lblCantidades.place(x=240, y=130)
        self.lblPrecios.place(x=310, y=130)
        self.lblVendida.place(x=380, y=130)

        self.lblNombre2.place(x=440, y=130)
        self.lblTalle2.place(x=550, y=130)
        self.lblCantidades2.place(x=640, y=130)
        self.lblPrecios2.place(x=710, y=130)
        self.lblVendida2.place(x=760, y=130)

        self.lblNombre3.place(x=820, y=130)
        self.lblTalle3.place(x=930, y=130)
        self.lblCantidades3.place(x=1020, y=130)
        self.lblPrecios3.place(x=1090, y=130)
        self.lblVendida3.place(x=1140, y=130)

        self.txtNombrePrenda.place(x=80, y=10)
        self.txtTallePrenda.place(x=80, y=40)
        self.txtCantidad.place(x=80, y=70)
        self.txtPrecio.place(x=80, y=100)

        self.btnAgregarPrenda.place(x=250, y=10)
        self.btnEditarPrenda.place(x=350, y=10)
        self.btnEliminarPrenda.place(x=450, y=10)
        self.btnGuardar.place(x=550, y=10)

    def agregar_prenda(self):
        nombre_prenda = self.txtNombrePrenda.get()
        talle_prenda = self.txtTallePrenda.get()

        if not nombre_prenda or not talle_prenda:
            messagebox.showerror("Error", "Por favor, complete la información de la prenda y el talle.")
            return

        try:
            cantidad = int(self.txtCantidad.get())
            precio = int(self.txtPrecio.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores válidos para cantidad y precio.")
            return

        nueva_prenda = Producto(nombre_prenda, cantidad, precio, talle_prenda)
        nueva_prenda.checkbox_state.set(False)  
        self.productos.append(nueva_prenda)
        self.mostrar_prendas_en_grilla()
        self.limpiar_campos()

    def mostrar_prendas_en_grilla(self):
        for etiqueta in self.etiquetas_prendas:
            etiqueta.destroy()

        for i, prenda in enumerate(self.productos):

            etiqueta_prenda = ttk.Label(root, text=prenda.nombre)
            etiqueta_prenda.place(x=10, y=150 + i * 30)

            etiqueta_talle = ttk.Label(root, text=prenda.talle)
            etiqueta_talle.place(x=160, y=150 + i * 30)

            etiqueta_cantidad = ttk.Label(root, text=prenda.cantidad)
            etiqueta_cantidad.place(x=260, y=150 + i * 30)

            etiqueta_precio = ttk.Label(root, text="$" + str(prenda.precio))
            etiqueta_precio.place(x=320, y=150 + i * 30)

            checkbox = ttk.Checkbutton(root, variable=prenda.checkbox_state)
            checkbox.place(x=400, y=150 + i * 30)

            self.etiquetas_prendas.append(etiqueta_prenda)

        if len(self.productos) > 20:
            # Añadir líneas a la derecha al superar 20
            for i, prenda in enumerate(self.productos[20:], start=20):

                etiqueta_prenda = ttk.Label(root, text=prenda.nombre)
                etiqueta_prenda.place(x=450, y=150 + (i - 20) * 30)

                etiqueta_talle = ttk.Label(root, text=prenda.talle)
                etiqueta_talle.place(x=560, y=150 + (i - 20) * 30)

                etiqueta_cantidad = ttk.Label(root, text=prenda.cantidad)
                etiqueta_cantidad.place(x=660, y=150 + (i - 20) * 30)

                etiqueta_precio = ttk.Label(root, text="$" + str(prenda.precio))
                etiqueta_precio.place(x=720, y=150 + (i - 20) * 30)

                checkbox = ttk.Checkbutton(root, variable=prenda.checkbox_state)
                checkbox.place(x=780, y=150 + (i - 20) * 30)
                self.etiquetas_prendas.append(etiqueta_prenda)

        if len(self.productos) >= 40:
            # Añadir líneas a la derecha al superar 40
            for i, prenda in enumerate(self.productos[40:], start=40):

                etiqueta_prenda = ttk.Label(root, text=prenda.nombre)
                etiqueta_prenda.place(x=830, y=150 + (i - 40) * 30)

                etiqueta_talle = ttk.Label(root, text=prenda.talle)
                etiqueta_talle.place(x=940, y=150 + (i - 40) * 30)

                etiqueta_cantidad = ttk.Label(root, text=prenda.cantidad)
                etiqueta_cantidad.place(x=1040, y=150 + (i - 40) * 30)

                etiqueta_precio = ttk.Label(root, text="$" + str(prenda.precio))
                etiqueta_precio.place(x=1100, y=150 + (i - 40) * 30)

                checkbox = ttk.Checkbutton(root, variable=prenda.checkbox_state)
                checkbox.place(x=1150, y=150 + (i - 40) * 30)
                self.etiquetas_prendas.append(etiqueta_prenda)

        root.update_idletasks()
        root.geometry(f"1080x{150 + max(len(self.productos), 20) * 30}")

    def limpiar_campos(self):
        self.txtNombrePrenda.delete(0, tk.END)
        self.txtCantidad.delete(0, tk.END)
        self.txtTallePrenda.delete(0, tk.END)
        self.txtPrecio.delete(0, tk.END)

    def guardar_prendas_en_csv(self):
        try:
            with open(self.archivo_csv, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['Prenda', 'Talle', 'Cantidad', 'Precio', 'Check']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for prenda in self.productos:
                    estado_check = "Realizado" if prenda.checkbox_state.get() else "No Realizado"
                    writer.writerow({'Prenda': prenda.nombre,
                                     'Talle': prenda.talle,
                                     'Cantidad': prenda.cantidad,
                                     'Precio': prenda.precio,
                                     'Check': estado_check})

            messagebox.showinfo("Guardado", "Archivo guardado.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar prendas y acciones: {str(e)}")

    def editar_prenda_dialogo(self):
        if not self.productos:
            messagebox.showerror("Error", "No hay prendas para editar.")
            return

        # Crear una lista de nombres de prendas para el cuadro de diálogo
        nombres_prendas = [prenda.nombre for prenda in self.productos]

        # Mostrar cuadro de diálogo para seleccionar la prenda a editar
        seleccion = simpledialog.askstring("Editar Prenda", "Seleccione la prenda a editar:", initialvalue=nombres_prendas[0], parent=root)

        if not seleccion:
            return

        # Encontrar la prenda seleccionada
        prenda_seleccionada = next((prenda for prenda in self.productos if prenda.nombre == seleccion), None)

        if prenda_seleccionada:
            # Mostrar cuadro de diálogo para editar la prenda
            nuevo_nombre = simpledialog.askstring("Editar Prenda", "Ingrese el nuevo nombre:", initialvalue=prenda_seleccionada.nombre, parent=root)
            nuevo_talle = simpledialog.askstring("Editar Prenda", "Ingrese el nuevo talle:", initialvalue=prenda_seleccionada.talle, parent=root)

            try:
                nueva_cantidad = int(simpledialog.askstring("Editar Prenda", "Ingrese la nueva cantidad:", initialvalue=prenda_seleccionada.cantidad, parent=root))
                nuevo_precio = int(simpledialog.askstring("Editar Prenda", "Ingrese el nuevo precio:", initialvalue=prenda_seleccionada.precio, parent=root))
            except ValueError:
                messagebox.showerror("Error", "Ingrese valores válidos para cantidad y precio.")
                return

            # Actualizar la prenda con los nuevos valores
            prenda_seleccionada.nombre = nuevo_nombre
            prenda_seleccionada.talle = nuevo_talle
            prenda_seleccionada.cantidad = nueva_cantidad
            prenda_seleccionada.precio = nuevo_precio

            # Actualizar la grilla
            self.mostrar_prendas_en_grilla()

    def eliminar_prenda(self):
        if not self.productos:
            messagebox.showerror("Error", "No hay prendas para eliminar.")
            return

        # Crear una lista de nombres de prendas para el cuadro de diálogo
        nombres_prendas = [prenda.nombre for prenda in self.productos]

        # Mostrar cuadro de diálogo para seleccionar la prenda a eliminar
        seleccion = simpledialog.askstring("Eliminar Prenda", "Seleccione la prenda a eliminar:", initialvalue=nombres_prendas[0], parent=root)

        if not seleccion:
            return

        # Encontrar la prenda seleccionada
        prenda_seleccionada = next((prenda for prenda in self.productos if prenda.nombre == seleccion), None)

        if prenda_seleccionada:
            # Confirmar la eliminación
            confirmacion = messagebox.askyesno("Eliminar Prenda", f"¿Está seguro que desea eliminar la prenda '{prenda_seleccionada.nombre}'?")

            if confirmacion:
                # Eliminar la prenda
                self.productos.remove(prenda_seleccionada)

                # Actualizar la grilla
                self.mostrar_prendas_en_grilla()

    def cargar_datos_desde_csv(self):
        try:
            with open(self.archivo_csv, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    nombre = row['Prenda']
                    talle = row['Talle']
                    cantidad = int(row['Cantidad'])
                    precio = int(row['Precio'])
                    check = row['Check'].lower() == 'realizado'

                    nueva_prenda = Producto(nombre, cantidad, precio, talle)
                    nueva_prenda.check = check
                    nueva_prenda.checkbox_state.set(check)
                    self.productos.append(nueva_prenda)

        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar datos desde CSV: {str(e)}")

    def crear_archivo_csv_si_no_existe(self):
        if not os.path.isfile(self.archivo_csv):
            try:
                with open(self.archivo_csv, 'w', newline='', encoding='utf-8') as csvfile:
                    fieldnames = ['Prenda', 'Talle', 'Cantidad', 'Precio', 'Check']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
            except Exception as e:
                messagebox.showerror("Error", f"Error al crear el archivo CSV: {str(e)}")

# Crear la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = ControlDeStockApp(root)
    root.mainloop()