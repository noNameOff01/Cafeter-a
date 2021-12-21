from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import back
from back import Valores
from back import Ventas as ven
from back import Login as lg
import sys


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(480, 581)
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setGeometry(QRect(0, 0, 480, 540))
        self.label_4.setAutoFillBackground(True)
        self.label_4.setText("")
        self.label_4.setPixmap(QPixmap("./Recursos/Imagenes/bgLogin.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setGeometry(QRect(60, 10, 360, 120))
        self.label_5.setStyleSheet("background-color:rgb(126, 110, 109);\n"
        "font: 48pt \"Vladimir Script\";\n"
        "border-radius: 10px;\n"
        "border: 5px soild #000000;")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.users = QLineEdit(self.centralwidget)
        self.users.setGeometry(QRect(100, 180, 280, 40))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.users.setFont(font)
        self.users.setStyleSheet("background:rgb(255, 219, 167);\n"
        "border-radius: 10px;\n"
        "Border:None;")
        self.users.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.users.setObjectName("users")
        self.password = QLineEdit(self.centralwidget)
        self.password.setGeometry(QRect(100, 280, 280, 40))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setStyleSheet("background:rgb(255, 219, 167);\n"
        "border-radius: 10px;\n"
        "Border:None;")
        self.password.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.password.setObjectName("password")
        self.password.setEchoMode(QLineEdit.Password)
        self.usuario_incorrecto = QLabel(self.centralwidget)
        self.usuario_incorrecto.setGeometry(QRect(100, 220, 180, 30))
        self.usuario_incorrecto.setStyleSheet("background-color: rgba(0, 0, 0 , 0%);\n"
        "font: 10pt \"Arial\";\n"
        "color:rgb(255, 0, 0);\n"
        "border:none;")
        self.usuario_incorrecto.setText("")
        self.usuario_incorrecto.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.usuario_incorrecto.setFixedWidth(300)
        self.usuario_incorrecto.setObjectName("usuario_incorrecto")
        self.contrasena_incorrecta = QLabel(self.centralwidget)
        self.contrasena_incorrecta.setGeometry(QRect(160, 320, 171, 51))
        self.contrasena_incorrecta.setStyleSheet("background-color: rgba(0, 0, 0 , 0%);\n"
        "font: 10pt \"Arial\";\n"
        "color:rgb(255, 0, 0);\n"
        "border:none;")
        self.contrasena_incorrecta.setText("")
        self.contrasena_incorrecta.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.contrasena_incorrecta.setObjectName("contrasena_incorrecta")
        self.bt_ingresar = QPushButton(self.centralwidget)
        self.bt_ingresar.setGeometry(QRect(195, 370, 90, 30))
        self.bt_ingresar.setStyleSheet("QPushButton{\n"
        "    \n"
        "        background-color:rgb(126, 110, 109);\n"
        "        font: 8pt \"MS Shell Dlg 2\";\n"
        "        color:rgb(255, 255, 255);\n"
        "        border-radius: 15px;\n"
        "border:1px soild #00007f;\n"
        "\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "    \n"
        "        background-color:rgb(67, 42, 37);\n"
        "        font: 8pt \"MS Shell Dlg 2\";\n"
        "        border-radius: 15px;\n"
        "border:1px soild #00007f;\n"
        "\n"
        "}\n"
        "")
        self.bt_ingresar.setObjectName("bt_ingresar")
        self.bt_ingresar.clicked.connect(self.iniciarSesion)
        self.datos = back.Login()
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setGeometry(QRect(160, 140, 160, 40))
        self.label_6.setStyleSheet("background-color: rgba(0, 0, 0 , 0%);\n"
        "font: 12pt \"Arial\";\n"
        "color:rgb(255, 255, 255);\n"
        "border:none;")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setGeometry(QRect(160, 240, 160, 40))
        self.label_3.setStyleSheet("background-color: rgba(0, 0, 0 , 0%);\n"
        "font: 12pt \"Arial\";\n"
        "color:rgb(255, 255, 255);\n"
        "border:none;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        Login.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Login)
        self.menubar.setGeometry(QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        Login.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QMetaObject.connectSlotsByName(Login)

    def iniciarSesion(self):
        self.contrasena_incorrecta.setText('')
        self.usuario_incorrecto.setText('')
        users_entry= self.users.text()
        password_entry= self.password.text()

        users_entry = str("'" + users_entry + "'")
        password_entry = str("'" + password_entry + "'")
        
        dato1 = self.datos.busca_users(users_entry)
        dato2 = self.datos.busca_password(password_entry)

        if dato1 == [] and dato2 == []:
            self.contrasena_incorrecta.setText('Contraseña incorrecta')
            self.usuario_incorrecto.setText('Usuario incorrecto')
        else:

            if dato1 == []:
                self.usuario_incorrecto.setText('Usuario incorrecto')
            else:
                dato1 = dato1[0][1]
            
            if dato2 == []:
                self.contrasena_incorrecta.setText('Contraseña incorrecta')
            else:
                dato2 = dato2[0][2]
            
            if dato1 != [] and dato2 !=[]:
                self.w = Window()
                self.w.show()

    def retranslateUi(self, Login):
        _translate = QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.label_5.setText(_translate("Login", "Iniciar Sesión"))
        self.users.setPlaceholderText(_translate("Login", "Ingrese su usuario"))
        self.password.setPlaceholderText(_translate("Login", "Ingrese su su contraseña"))
        self.bt_ingresar.setText(_translate("Login", "Continuar"))
        self.label_6.setText(_translate("Login", "Usuario"))
        self.label_3.setText(_translate("Login", "Contraseña"))

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tipoCafe = Valores.tipoCafe(self)
        self.sabor = Valores.sabor(self)
        self.tamanio = Valores.tamanio(self)
        self.tipoLeche = Valores.tipoLeche(self)
        self.extras = Valores.extras(self)
        self.tipoPedido = Valores.tipoPedido(self)
        self.horas, self.ventasH = ven.ventasD(self)
        self.filasVentasDia = len(self.horas)
        self.semanas, self.ventasM = ven.ventasM(self)
        self.filasVentasMes = len(self.semanas)
        self.anchoWPedido = 180
        self.largoWPedido = 70
        cAdminP = back.Productos()
        #self.admin, self.contrasenia = lg.valores(self)

        # ------ VENTANA PRINCIPAL ------
        # Modificación de las propiedades
        self.setWindowTitle('Cafeteria') # Título de la ventana
        self.setStyleSheet('background-color: white;') # Color de fondo
        self.Width = 800 # Ancho
        self.height = int(0.618 * self.Width) # Largo
        self.resize(self.Width, self.height) # Modificación del tamaño

        # ---- INICIALIZACION DE WIDGETS ----
        # Fuentes
        self.negrita14 = QFont('Arial', 14)
        self.fuenteNegrita10 = QFont('Arial', 10)
        self.fuenteCursiva = QFont('Arial', 20, 10, True)
        self.negrita14.setBold(True)
        self.fuenteNegrita10.setBold(True)

        # Botones
        self.btnPedidos = QPushButton('Pedido') # Botón Pedido
        self.btnInventario = QPushButton('Inventario') # Botón Inventario
        self.btnVentas = QPushButton('Ventas') # Botón Ventas
        self.btnAdminMatP = QPushButton('Admin. Materia Prima')
        self.btnAdminUsuarios = QPushButton('Admin. Usuarios')
        self.btnAdminProductos = QPushButton('Admin. Productos')
        self.btnFinalizarP = QPushButton('Finalizar Pedido', objectName = 'btnFinalizarP')  # Botón Finalizar
        self.btnAgregarP = QPushButton('Agregar Pedido', objectName = 'btnAgregarP')
        self.btnAgregar = QPushButton('Agregar', objectName = 'agregar')
        self.btnEliminar = QPushButton('Eliminar', objectName = 'eliminar')
        self.btnAceptar1 = QPushButton('Aceptar', objectName = 'btnAceptar1')
        self.btnAceptar2 = QPushButton('Aceptar', objectName = 'btnAceptar2')
        self.btnIngresar = QPushButton('Ingresar', objectName = 'btnIngresar')
        self.btnAgregarUser = QPushButton('Agregar', objectName = 'btnAgregarUser')
        self.btnEliminarUser = QPushButton('Eliminar/Modificar', objectName = 'btnEliminarUser')
        self.btnModificarUser = QPushButton('Modificar', objectName = 'btnModificarUser')
        self.btnEjecutarAgregar = QPushButton('Ejecutar', objectName = 'btnEjecutarAgregar')
        self.btnEjecutarEliminar = QPushButton('Ejecutar', objectName = 'btnEjecutarEliminar')
        self.btnEjecutarModificar = QPushButton('Ejecutar', objectName = 'btnEjecutarModificar')
        self.btnAceptarModificar = QPushButton('Aceptar', objectName = 'btnAceptarModificar')
        self.btnIngresarAdminProd = QPushButton('Ingresa', objectName = 'btnIngresarAdminProd')
        self.btnDelAddProductos = QPushButton('Agregar/Eliminar', objectName = 'btnDelAddProductos')
        self.btnEjecutarAgregarP = QPushButton('Ejecutar', objectName = 'btnEjecutarAgregarP')
        self.btnEjecutarEliminarP = QPushButton('Ejecutar', objectName = 'btnEjecutarEliminarP')
        self.btnAutenticarMatP = QPushButton('Ingresar', objectName = 'btnAutenticarMatP')
        
        # Combo box
        self.btnTipoCafe = QComboBox(objectName = 'btnTipoCafe') # Menú desplegable "Tipo de Café"
        self.btnSabor = QComboBox(objectName = 'btnSabor') # Menú desplegable "Sabor"
        self.btnTamanio = QComboBox(objectName = 'btnTamanio') # Menú desplegable "Tamaño"
        self.btnTipoLeche = QComboBox(objectName = 'btnTipoLeche') # Menú desplegable "Tipo de Leche"
        self.btnExtras = QComboBox(objectName = 'btnExtras') # Menú desplegable "Extras"
        self.btnTipoPedido = QComboBox(objectName = 'btnTipoPedido') # Menú desplegable "Tipo de Pedido"
        self.comboCategoriaModificar = QComboBox(objectName = 'comboCategoriaModificar')
        self.comboOpcionesModificar = QComboBox(objectName = 'comboOpcionesModificar')
        self.comboUsuario = QComboBox(objectName = 'comboUsuario')

        # Campos de texto
        self.cNombreCliente = QLineEdit(objectName = 'cNombreCliente') # Campo de texto "Nombre del cliente"
        self.cT1 = QLineEdit(objectName = 'cT1')
        self.cT2 = QLineEdit(objectName = 'cT2')
        self.cT3 = QLineEdit(objectName = 'cT3')
        self.cT4 = QLineEdit(objectName = 'cT4')
        self.campoUsuario = QLineEdit(objectName = 'campoUsuario')
        self.campoContrasenia = QLineEdit(objectName = 'campoContrasenia')
        self.campoNombreAgregar = QLineEdit(objectName = 'campoNombreAgregar')
        self.campoUsuarioAgregar = QLineEdit(objectName = 'campoUsuarioAgregar')
        self.campoContraseniaAgregar = QLineEdit(objectName = 'campoContraseniaAgregar')
        self.campoTipoAgregar = QLineEdit(objectName = 'campoTipoAgregar')
        self.campoValorModificar = QLineEdit(objectName = 'campoValorModificar')
        self.campoUsuarioProductos = QLineEdit(objectName = 'campoUsuarioProductos')
        self.campoContraseniaProductos = QLineEdit(objectName = 'campoContraseniaProductos')
        self.campoIdProductos = QLineEdit(objectName = 'campoIdProductos')
        self.campoNombreProductos = QLineEdit(objectName = 'campoNombreProductos')
        self.campoIdProductosE = QLineEdit(objectName = 'comboIdProductos')
        self.campoUsuarioMatP = QLineEdit(objectName = 'campoUsuarioMatP')
        self.campoContraseniaMatP = QLineEdit(objectName = 'campoContraseniaMatP')

        self.cNombreCliente.setPlaceholderText('Nombre del Cliente')
        self.campoUsuario.setPlaceholderText('Usuario')
        self.campoContrasenia.setPlaceholderText('Contraseña')
        self.campoUsuarioProductos.setPlaceholderText('Usuario')
        self.campoContraseniaProductos.setPlaceholderText('Contraseña')
        self.campoIdProductos.setPlaceholderText('ID')
        self.campoNombreProductos.setPlaceholderText('Nombre')
        self.campoNombreAgregar.setPlaceholderText('Nombre')
        self.campoUsuarioAgregar.setPlaceholderText('Usuario')
        self.campoContraseniaAgregar.setPlaceholderText('Contraseña')
        self.campoTipoAgregar.setPlaceholderText('Tipo')
        self.campoValorModificar.setPlaceholderText('Valor')
        self.campoIdProductosE.setPlaceholderText('Id Producto a eliminar')
        self.campoUsuarioMatP.setPlaceholderText('Usuario')
        self.campoContraseniaMatP.setPlaceholderText('Contraseña')

        self.campoUsuario.setEnabled(False)
        self.campoContrasenia.setEnabled(False)
        self.campoUsuario.setEnabled(False)
        self.campoNombreAgregar.setEnabled(False)
        self.campoUsuarioAgregar.setEnabled(False)
        self.campoContraseniaAgregar.setEnabled(False)
        self.campoTipoAgregar.setEnabled(False)
        self.campoValorModificar.setEnabled(False)

        #Etiquetas
        self.logoCafe = QLabel('') # Logo del Café
        self.pedidoLabel = QLabel('Pedidos')
        self.inventarioLabel = QLabel('Inventario')
        self.materiaPrimaLabel = QLabel('Administración de Materia Prima')
        self.adminUsuariosLabel = QLabel('Administración de Usuarios')
        self.adminProductosLabel = QLabel('Administración de Productos')
        self.autenticarUsuariosLabel = QLabel('')
        self.confirmacionUsuariosLabel = QLabel('')
        self.lAutenticarUsuariosP = QLabel('')
        self.lConfirmacionOperacionP = QLabel('')
        self.spacer1 = QLabel('')
        self.label2 = QLabel('')
        self.label3 = QLabel('')
        self.label4 = QLabel('')
        self.label5 = QLabel('')
        self.ventasLabel = QLabel('Ventas')
        self.ventasDiaL = QLabel('Ventas por día')
        self.ventasMesL = QLabel('Ventas por mes')
        self.spacer = QLabel('')
        self.eliminarUsers = QLabel('Eliminar')
        self.modificarUser = QLabel('Modificar')
        self.pixmapCafe = QPixmap('./Recursos/Imagenes/logoCafe.png')
        self.pixmapCafe.scaled(20, 20)
        self.logoCafe.setPixmap(self.pixmapCafe)
        self.pedidoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Items de Combobox
        self.btnTipoCafe.addItem('Tipo de Café')
        self.btnTipoCafe.addItems(self.tipoCafe)
        self.btnSabor.addItem('Sabor')
        self.btnSabor.addItems(self.sabor)
        self.btnTamanio.addItem('Tamaño')
        self.btnTamanio.addItems(self.tamanio)
        self.btnTipoLeche.addItem('Tipo de Leche')
        self.btnTipoLeche.addItems(self.tipoLeche)
        self.btnExtras.addItem('Extras')
        self.btnExtras.addItems(self.extras)
        self.btnTipoPedido.addItem('Tipo de Pedido')
        self.btnTipoPedido.addItems(self.tipoPedido)

        # Desactivando Items de QComboBox
        self.btnTipoCafe.model().item(0).setEnabled(False)
        self.btnSabor.model().item(0).setEnabled(False)
        self.btnTamanio.model().item(0).setEnabled(False)
        self.btnTipoLeche.model().item(0).setEnabled(False)
        self.btnExtras.model().item(0).setEnabled(False)
        self.btnTipoPedido.model().item(0).setEnabled(False)

        # Tablas
        self.tablaAMateriaPrima = QTableWidget(4, 3)
        self.tablaUsuarios = QTableWidget(3, 2)

        self.tablaAMateriaPrima.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaUsuarios.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # ESTTILOS
        # Hojas de Estilos
        self.btnPedidos.setStyleSheet('border: none; color: white;')
        self.btnAdminMatP.setStyleSheet('border: none;\ncolor: white;')
        self.btnInventario.setStyleSheet('border: none; color: white;')
        self.btnVentas.setStyleSheet('border: none; color: white;')
        self.btnAdminUsuarios.setStyleSheet('border: none;\ncolor: white;')
        self.btnAdminProductos.setStyleSheet('border: none;\ncolor: white;')
        self.pedidoSS = """
                            QComboBox { 
                                        border-radius: 10px; 
                                        color: white;
                                        }

                            QLineEdit {
                                    border: 1px solid #d4c3b8;
                                    border-radius: 5px;
                                    background-color: #d4c3b8;
                                    color: black;
                                    }

                            QPushButton {
                                    border: 1px solid brown;
                                    border-radius: 5px;
                                    background-color: brown;
                                    color: white;
                            }
                            
                            QLabel {
                                font: 48pt \"Vladimir Script\";
                                color: #6b350a;
                            }

                            QComboBox#btnTipoCafe {
                                background-color: rgb(255, 87, 87); 
                            }
                            
                            QComboBox#btnSabor {
                                background-color: rgb(228, 194, 20); 
                            }

                            QComboBox#btnTamanio {
                                background-color: rgb(255, 22, 22); 
                            }
                            
                            QComboBox#btnTipoLeche {
                                background-color: rgb(138, 189, 65); 
                            }
                            
                            QComboBox#btnExtras {
                                background-color: rgb(140, 82, 255); 
                            }

                            QComboBox#btnTipoPedido {
                                background-color: rgb(63, 223, 194); 
                            }

                            QPushButton#btnFinalizarP {
                                background-color: rgb(150, 22, 22);
                            }

                            QPushButton#btnAgregarP {
                                background-color: rgb(150, 22, 22);
                            }
                                """
        self.comboAdminUsuariosSS = """
                                    border-radius: 5px;
                                    border: 1px solid #6b350a;
                                    background-color: #d4c3b8;
                                    color: #6b350a;
                                    font: 14pt \"Arial\";
                                    """
        self.inventarioLabel.setStyleSheet('font: 48pt \"Vladimir Script\";\ncolor: #6b350a;')
        self.materiaPrimaLabel.setStyleSheet('font: 48pt \"Vladimir Script\";\ncolor: #6b350a;')
        self.adminUsuariosLabel.setStyleSheet('font: 48pt \"Vladimir Script\";\ncolor: #6b350a;')
        self.adminProductosLabel.setStyleSheet('font: 48pt \"Vladimir Script\";\ncolor: #6b350a;')
        self.adminUsuariosSS = """
                                    QLineEdit { 
                                        background-color: white; 
                                        color: white; 
                                        border: none;
                                        font: 14pt \"Arial\";
                                    }

                                    QPushButton {
                                        border-radius: 5px;
                                        background-color: rgb(150, 22, 22);
                                        border: 1px solid rgb(150, 22, 22);
                                        color: white;
                                        font: 14pt \"Arial\";
                                    }

                                    QComboBox {
                                        border: none;
                                        color: white;
                                        background-color: white;
                                    }

                                    QComboBox::drop-down {
                                        border-left-color: white;
                                    }

                                    QPushButton#btnIngresar {
                                        background-color: white;
                                        color: white;
                                        border: none
                                    }

                                    QPushButton#btnEjecutarAgregar {
                                        background-color: white;
                                        color: white;
                                        border: none
                                    }

                                    QPushButton#btnEjecutarEliminar {
                                        background-color: white;
                                        color: white;
                                        border: none
                                    }

                                    QPushButton#btnAceptarModificar {
                                        background-color: white;
                                        color: white;
                                        border: none
                                    }

                                    QPushButton#btnEjecutarModificar {
                                        background-color: white;
                                        color: white;
                                        border: none
                                    }
                                """
        self.comboEliminarUsers = """
                                    border: 1px solid #6b350a;
                                    background-color: white;
                                    color: #6b350a;
                                    font: 14pt \"Arial\";
                                    border-radius: 5px;
                                """
        self.adminProductosSS = """
                                    QLabel {
                                        color: white;
                                        font: 14pt \"Arial\"
                                    }

                                    QPushButton {
                                        border: none;
                                        background-color: white;
                                        color: white;
                                    }

                                    QLineEdit {
                                        border: none;
                                        color: white;
                                        background-color: white
                                    }

                                    QComboBox { 
                                        border: none;
                                        color: white;
                                        background-color: white;
                                    }

                                    QComboBox::drop-down {
                                        border-left-color: white;
                                    }

                                    QPushButton#btnDelAddProductos {
                                        border-radius: 5px;
                                        background-color: rgb(150, 22, 22);
                                        border: 1px solid rgb(150, 22, 22);
                                        color: white;
                                        font: 14pt \"Arial\";
                                    }
                                """

        # Configuración de Fuentes de los Widgets
        self.btnPedidos.setFont(self.negrita14) # -> Inicia Conf. QPushButton
        self.btnInventario.setFont(self.negrita14)
        self.btnVentas.setFont(self.negrita14)
        self.btnAdminMatP.setFont(self.negrita14)
        self.btnAdminUsuarios.setFont(self.negrita14)
        self.btnAdminProductos.setFont(self.negrita14)
        self.btnFinalizarP.setFont(self.negrita14) 
        self.btnAgregarP.setFont(self.negrita14) # <- Termina Conf. QPushButton
        self.btnTipoCafe.setFont(self.negrita14) # -> Inicia Conf. QComboBox
        self.btnSabor.setFont(self.negrita14)
        self.btnTamanio.setFont(self.negrita14)
        self.btnTipoLeche.setFont(self.negrita14)
        self.btnExtras.setFont(self.negrita14)
        self.btnTipoPedido.setFont(self.negrita14)
        self.cNombreCliente.setFont(self.negrita14) # <- Termina Conf. QComboBox
        self.ventasDiaL.setFont(self.negrita14) # -> Inicia Conf. QLabel
        self.ventasMesL.setFont(self.negrita14) # -> Termina Conf. QLablel

        #Configuración de tamaño de los Widgets
        self.btnPedidos.setFixedSize(260, 50) # -> Inicia Conf. QPushButton
        self.btnInventario.setFixedSize(260, 50)
        self.btnVentas.setFixedSize(260, 50)
        self.btnAdminMatP.setFixedSize(260, 50)
        self.btnAdminUsuarios.setFixedSize(260, 50)
        self.btnAdminProductos.setFixedSize(260, 50)
        self.btnIngresar.setFixedWidth(120)
        self.btnFinalizarP.setFixedSize(self.anchoWPedido, self.largoWPedido)
        self.btnAgregarP.setFixedSize(self.anchoWPedido, self.largoWPedido) # <- Termina Conf. QPushButton
        self.btnTipoCafe.setFixedSize(self.anchoWPedido, self.largoWPedido) # -> Inicia conf. QComboBox
        self.btnSabor.setFixedSize(self.anchoWPedido, self.largoWPedido)
        self.btnTamanio.setFixedSize(self.anchoWPedido, self.largoWPedido)
        self.btnTipoLeche.setFixedSize(self.anchoWPedido, self.largoWPedido)
        self.btnExtras.setFixedSize(self.anchoWPedido, self.largoWPedido)
        self.btnTipoPedido.setFixedSize(self.anchoWPedido, self.largoWPedido)
        self.cNombreCliente.setFixedSize(self.anchoWPedido, self.largoWPedido) # <- Termina Conf. QComboBox
        self.logoCafe.setFixedSize(260, 200) # -> Inicia Conf. QLabel
        self.pedidoLabel.setFixedSize(1290, 100)
        self.autenticarUsuariosLabel.setFixedHeight(50)
        self.lAutenticarUsuariosP.setFixedHeight(50)
        self.btnAgregarUser.setFixedSize(100, 50)
        self.campoNombreAgregar.setFixedWidth(350)
        self.campoUsuarioAgregar.setFixedWidth(350)
        self.campoContraseniaAgregar.setFixedWidth(350)
        self.campoTipoAgregar.setFixedWidth(350)
        self.btnEjecutarAgregar.setFixedSize(100, 50)
        self.btnEliminarUser.setFixedSize(200, 50)
        self.comboUsuario.setFixedWidth(175)
        self.btnEjecutarEliminar.setFixedSize(100, 50)
        self.campoValorModificar.setFixedWidth(350)
        self.spacer.setFixedSize(40, 20)
        self.campoUsuarioProductos.setFixedWidth(350)
        self.campoContraseniaProductos.setFixedWidth(350)
        self.btnIngresarAdminProd.setFixedWidth(120)
        self.btnDelAddProductos.setFixedSize(200, 50)
        self.campoIdProductos.setFixedWidth(350)
        self.campoNombreProductos.setFixedWidth(350)
        self.btnEjecutarAgregarP.setFixedSize(180, 40)
        self.campoIdProductosE.setFixedWidth(350)
        self.btnEjecutarEliminarP.setFixedSize(180, 40)
        
        # Alineación
        self.inventarioLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ventasLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.materiaPrimaLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.adminProductosLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.adminUsuariosLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.autenticarUsuariosLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        #Configuración de iconos
        self.btnPedidos.setIcon(QIcon('./Recursos/Iconos/tCafe.png'))
        self.btnInventario.setIcon(QIcon('./Recursos/Iconos/inventario.png'))
        self.btnVentas.setIcon(QIcon('./Recursos/Iconos/ventas.png'))
        self.btnAdminMatP.setIcon(QIcon('./Recursos/Iconos/materiaPrima.png'))
        self.btnAdminProductos.setIcon(QIcon('./Recursos/Iconos/productos.png'))
        self.btnAdminUsuarios.setIcon(QIcon('./Recursos/Iconos/usuario.png'))
        self.btnPedidos.setIconSize(QSize(35, 35))
        self.btnInventario.setIconSize(QSize(35, 35))
        self.btnVentas.setIconSize(QSize(35, 35))
        self.btnAdminMatP.setIconSize(QSize(35, 35))
        self.btnAdminProductos.setIconSize(QSize(35, 35))
        self.btnAdminUsuarios.setIconSize(QSize(35, 35))

        # Opciones para tablas
        self.tablaUsuarios.setHorizontalHeaderLabels(['Nombre', 'Privilegio'])

        # Manejadores de eventos para páginas
        self.btnPedidos.clicked.connect(self.botonPedidos)
        self.btnInventario.clicked.connect(self.botonInventario)
        self.btnVentas.clicked.connect(self.botonVentas)
        self.btnAdminMatP.clicked.connect(self.botonAdminMatP)
        self.btnAdminUsuarios.clicked.connect(self.botonAdminUsuarios)
        self.btnAdminProductos.clicked.connect(self.botonAdminProductos)
        self.btnAgregar.clicked.connect(self.btn_Agregar)
        self.btnEliminar.clicked.connect(self.btn_Eliminar)
        self.btnAgregarUser.clicked.connect(self.btn_agregarUser)
        self.btnEliminarUser.clicked.connect(self.btn_EliminarUser)
        self.btnIngresar.clicked.connect(self.btn_Ingresar)
        self.btnEjecutarAgregar.clicked.connect(self.btn_EjecutarAgregar)
        self.btnEjecutarEliminar.clicked.connect(self.btn_EjecutarEliminar)
        self.btnEjecutarModificar.clicked.connect(self.btn_EjecutarModificar)
        self.btnDelAddProductos.clicked.connect(self.btn_DelAddProductos)
        self.btnIngresarAdminProd.clicked.connect(self.btn_IngresarAdminProd)
        self.btnEjecutarAgregarP.clicked.connect(self.btn_EjecutarAgregarP)
        self.btnEjecutarEliminarP.clicked.connect(self.btn_EjecutarEliminarP)

        # Pestañas
        self.tab1 = self.ventanaPedidos()
        self.tab2 = self.ventanaInventario()
        self.tab3 = self.ventanaVentas()
        self.tab4 = self.ventanaAdminMatP()
        self.tab5 = self.administracionUsuarios()
        self.tab6 = self.administracionProductos()

        self.principal() # Se llama a la pestaña principal
        self.showMaximized() # Despliega "maximizada la pantalla principal"

    def principal(self):
        left_layout = QVBoxLayout() # Layout Vertical
        left_layout.addWidget(self.logoCafe) # Imagen del logo del café
        left_layout.addSpacerItem(QSpacerItem(260, 15))
        left_layout.addWidget(self.btnPedidos) # Botón para página Pedidos
        left_layout.addWidget(self.btnInventario) # Botón para página inventario
        left_layout.addWidget(self.btnVentas) # Botón para página ventas
        left_layout.addWidget(self.btnAdminMatP)
        left_layout.addWidget(self.btnAdminUsuarios)
        left_layout.addWidget(self.btnAdminProductos)
        left_layout.addStretch(5) # Alineado desde bottom a top
        left_widget = QWidget() # Intancia de la clase QWidget
        left_widget.setStyleSheet('background-color: #6b350a;')
        left_widget.setFixedWidth(260)
        left_widget.setLayout(left_layout) # Se define el layout del documento

        self.right_widget = QTabWidget() 
        self.right_widget.tabBar().setObjectName("mainTab")

        self.right_widget.addTab(self.tab1, '')
        self.right_widget.addTab(self.tab2, '')
        self.right_widget.addTab(self.tab3, '')
        self.right_widget.addTab(self.tab4, '')
        self.right_widget.addTab(self.tab5, '')
        self.right_widget.addTab(self.tab6, '')

        self.right_widget.setCurrentIndex(0)
        self.right_widget.setStyleSheet('''QTabBar::tab{width: 0; \
            height: 0; margin: 0; padding: 0; border: none; background-color: red}''')

        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(self.right_widget)
        main_layout.setStretch(0, 40)
        main_layout.setStretch(1, 200)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    # Botones
    def botonPedidos(self):
        self.right_widget.setCurrentIndex(0)
        self.btnPedidos.setStyleSheet('background-color: #896950; border: none; color: white;')
        self.btnInventario.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnVentas.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminMatP.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminUsuarios.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminProductos.setStyleSheet('background-color: #6b350a; border: none; color: white;')

    def botonInventario(self):
        self.right_widget.setCurrentIndex(1)
        self.btnPedidos.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnInventario.setStyleSheet('background-color: #896950; border: none; color: white;')
        self.btnVentas.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminMatP.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminUsuarios.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminProductos.setStyleSheet('background-color: #6b350a; border: none; color: white;')

    def botonVentas(self):
        self.right_widget.setCurrentIndex(2)
        self.btnPedidos.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnInventario.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnVentas.setStyleSheet('background-color: #896950; border: none; color: white;')
        self.btnAdminMatP.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminUsuarios.setStyleSheet('background-color: #6b350a; border: none; color: white;')
    
    def botonAdminMatP(self):
        self.right_widget.setCurrentIndex(3)
        self.btnPedidos.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnInventario.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnVentas.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminMatP.setStyleSheet('background-color: #896950; border: none; color: white;')
        self.btnAdminUsuarios.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminProductos.setStyleSheet('background-color: #6b350a; border: none; color: white;')

    def botonAdminUsuarios(self):
        self.right_widget.setCurrentIndex(4)
        self.btnPedidos.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnInventario.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnVentas.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminMatP.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminUsuarios.setStyleSheet('background-color: #896950; border: none; color: white;')
        self.btnAdminProductos.setStyleSheet('background-color: #6b350a; border: none; color: white;')

    def botonAdminProductos(self):
        self.right_widget.setCurrentIndex(5)
        self.btnPedidos.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnInventario.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnVentas.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminMatP.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminUsuarios.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminProductos.setStyleSheet('background-color: #896950; border: none; color: white;')
    
    def btn_Agregar(self):
        self.label2.setText('ID')
        self.label3.setText('Nombre')
        self.label4.setText('Categoría')

        self.label2.setFont(self.negrita14)
        self.label3.setFont(self.negrita14)
        self.label4.setFont(self.negrita14)

        self.cT1.setEnabled(True)
        self.cT2.setEnabled(True)
        self.cT3.setEnabled(True)

        self.cT1.setStyleSheet('border: 1px solid black;\nborder-radius: 5px;')
        self.cT2.setStyleSheet('border: 1px solid black;\nborder-radius: 5px;')
        self.cT3.setStyleSheet('border: 1px solid black;\nborder-radius: 5px;')

        self.cT1.setFont(self.negrita14)
        self.cT2.setFont(self.negrita14)
        self.cT3.setFont(self.negrita14)

        self.btnAceptar1.setStyleSheet('border: 1px solid brown;\nborder-radius: 5px;\nbackground-color: brown;\ncolor: white;')
        self.btnAceptar1.setEnabled(True)
        
    def btn_Eliminar(self):
        self.label5.setText('ID')
        self.label5.setFont(self.negrita14)

        self.cT4.setEnabled(True)
        self.cT4.setStyleSheet('border: 1px solid black; border-radius: 5px;')
        self.cT4.setFont(self.negrita14)

        self.btnAceptar2.setStyleSheet('border: 1px solid brown;\nborder-radius: 5px;\nbackground-color: brown;\ncolor: white;')
        self.btnAceptar2.setEnabled(True)
	
    def btn_agregarUser(self):
        self.campoNombreAgregar.setEnabled(True)
        self.campoUsuarioAgregar.setEnabled(True)
        self.campoContraseniaAgregar.setEnabled(True)
        self.campoTipoAgregar.setEnabled(True)
        self.btnEjecutarAgregar.setStyleSheet("""
                                                border-radius: 5px;
                                                background-color: rgb(150, 22, 22);
                                                border: 1px solid rgb(150, 22, 22);
                                                color: white;
                                                font: 14pt \"Arial\";""")

        self.campoNombreAgregar.setStyleSheet(self.comboAdminUsuariosSS)
        self.campoUsuarioAgregar.setStyleSheet(self.comboAdminUsuariosSS)
        self.campoContraseniaAgregar.setStyleSheet(self.comboAdminUsuariosSS)
        self.campoTipoAgregar.setStyleSheet(self.comboAdminUsuariosSS)

    def btn_EliminarUser(self):
        self.autenticarUsuariosLabel.setText('Debe ser administrador para modificar o eliminar usuarios')
        self.autenticarUsuariosLabel.setStyleSheet('color: red;\nfont: 14pt \"Arial\"')
        
        self.campoUsuario.setEnabled(True)
        self.campoContrasenia.setEnabled(True)

        self.campoUsuario.setStyleSheet('background-color: #d4c3b8;\ncolor: #6b350a;\nborder: 1px solid #6b350a;\nborder-radius: 5px;')
        self.campoContrasenia.setStyleSheet('background-color: #d4c3b8;\ncolor: #6b350a;\nborder: 1px solid #6b350a;\nborder-radius: 5px;')

        self.btnIngresar.setEnabled(True)
        self.btnIngresar.setStyleSheet("""border-radius: 5px;\nbackground-color: rgb(150, 22, 22);\nborder: 1px solid rgb(150, 22, 22);
                                        color: white;\nfont: 14pt \"Arial\";""")

    def btn_Ingresar(self):
        self.usuarioUsers = self.campoUsuario.text()
        self.contraseniaUsers = self.campoContrasenia.text()
        
        self.correcto, self.gerente = back.Autenticacion.autenticar(self, self.usuarioUsers, self.contraseniaUsers)
        
        if self.correcto and self.gerente:
            self.eliminarUsers.setStyleSheet('color: brown;\nfont: 14pt \"Arial\"')
            self.modificarUser.setStyleSheet('color: brown;\nfont: 14pt \"Arial\"')
            self.comboUsuario.setStyleSheet(self.comboEliminarUsers)
            self.comboCategoriaModificar.setStyleSheet(self.comboEliminarUsers)
            self.comboOpcionesModificar.setStyleSheet(self.comboEliminarUsers)
        
            self.campoValorModificar.setEnabled(True)
            self.campoValorModificar.setStyleSheet(self.comboAdminUsuariosSS)

            self.btnEjecutarModificar.setStyleSheet("""border-radius: 5px;\nbackground-color: rgb(150, 22, 22);
                                                    \nborder: 1px solid rgb(150, 22, 22);\ncolor: white;\nfont: 14pt \"Arial\";""")
            self.btnEjecutarEliminar.setStyleSheet("""border-radius: 5px;\nbackground-color: rgb(150, 22, 22);
                                                    \nborder: 1px solid rgb(150, 22, 22);\ncolor: white;\nfont: 14pt \"Arial\";""")
            self.btnAceptarModificar.setStyleSheet("""border-radius: 5px;\nbackground-color: rgb(150, 22, 22);
                                                    \nborder: 1px solid rgb(150, 22, 22);\ncolor: white;\nfont: 14pt \"Arial\";""")
        else:
            self.autenticarUsuariosLabel.setText('El usuario o la contraseña son incorrectos')
        
    def btn_EjecutarAgregar(self):
        self.nombre = self.campoNombreAgregar.text()
        self.usuario = self.campoUsuarioAgregar.text()
        self.contrasenia = self.campoContraseniaAgregar.text()
        self.tipo = self.campoTipoAgregar.text()

    def btn_EjecutarEliminar(self):
        self.comboIndiceUser = self.comboUsuario.currentIndex()
        print(self.comboIndiceUser)

    def btn_EjecutarModificar(self):
        self.categoria = self.comboCategoriaModificar.currentIndex()
        self.opciones = self.comboOpcionesModificar.currentIndex()
        self.valor = self.campoValorModificar.text()
    
    def btn_DelAddProductos(self):
        self.campoUsuarioProductos.setEnabled(True)
        self.campoContraseniaProductos.setEnabled(True)
        self.btnIngresarAdminProd.setEnabled(True)

        self.lAutenticarUsuariosP.setStyleSheet('color: red;')
        self.lAutenticarUsuariosP.setText('Debe ser usuario o administrador para agregar o eliminar')    
        self.campoUsuarioProductos.setStyleSheet(self.comboAdminUsuariosSS)
        self.campoContraseniaProductos.setStyleSheet(self.comboAdminUsuariosSS)
        self.btnIngresarAdminProd.setStyleSheet("""border-radius: 5px;\nbackground-color: rgb(150, 22, 22);
                                                border: 1px solid rgb(150, 22, 22);\ncolor: white;
                                                font: 14pt \"Arial\";""")

    def btn_IngresarAdminProd(self):
        self.usuarioProd = self.campoUsuarioProductos.text()
        self.contraseniaProd = self.campoContraseniaProductos.text()

        self.autenticacion, self.administrador = back.Productos.credenciales(self, self.usuarioProd, self.contraseniaProd)

        if self.autenticacion and self.administrador:
            self.campoIdProductos.setEnabled(True)
            self.campoNombreProductos.setEnabled(True)
            self.btnEjecutarAgregarP.setEnabled(True)
            self.campoIdProductosE.setEnabled(True)
            self.btnEjecutarEliminarP.setEnabled(True)

            self.labelAgregarP.setStyleSheet('color: red')
            self.campoNombreProductos.setStyleSheet(self.comboAdminUsuariosSS)
            self.campoIdProductos.setStyleSheet(self.comboAdminUsuariosSS)
            self.btnEjecutarAgregarP.setStyleSheet("""border-radius: 5px;\nbackground-color: rgb(150, 22, 22);
                                                    border: 1px solid rgb(150, 22, 22);\ncolor: white;
                                                    font: 14pt \"Arial\";""")
            self.labelEliminarP.setStyleSheet('color: red')
            self.campoIdProductosE.setStyleSheet("""border-radius: 5px;\nborder: 1px solid #6b350a;
                                                background-color: #d4c3b8;\ncolor: #6b350a;
                                                font: 14pt \"Arial\";""")
            self.btnEjecutarEliminarP.setStyleSheet("""border-radius: 5px;\nbackground-color: rgb(150, 22, 22);
                                                    border: 1px solid rgb(150, 22, 22);\ncolor: white;
                                                    font: 14pt \"Arial\";""")
        else:
            self.lAutenticarUsuariosP.setText('Credenciales inválidas o no es administrador')
    
    def btn_EjecutarAgregarP(self):
        self.valoresComboA = back.Productos.valoresCombo(self)
        self.id = self.campoIdProductos.text()
        self.nombre = self.campoNombreProductos.text()

        filas = self.tablaAdminProductos.rowCount()
        self.tablaAdminProductos.insertRow(filas)

        self.tablaAdminProductos.setItem(filas, 0, QTableWidgetItem(self.id))
        self.tablaAdminProductos.setItem(filas, 1, QTableWidgetItem(self.nombre))

        back.Productos.agregarP(self, self.id, self.nombre)

    def btn_EjecutarEliminarP(self):
        self.eliminar = str(self.campoIdProductosE.text())
        nFilas = self.tablaAdminProductos.rowCount()
        self.indices = dict()
        
        for i in range(0, nFilas):
            self.indices[self.tablaAdminProductos.item(i, 0).text()] = i
        
        self.tablaAdminProductos.removeRow(self.indices[self.eliminar])
        back.Productos.eliminarP(self, self.eliminar)

    # Páginas
    def ventanaPedidos(self):
        main_layout = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()

        hbox.addWidget(self.btnTipoCafe)
        hbox.addWidget(self.btnSabor)
        hbox.addWidget(self.btnTamanio)
        
        hbox1.addWidget(self.btnTipoLeche)
        hbox1.addWidget(self.btnExtras)
        hbox1.addWidget(self.btnTipoPedido)
        
        hbox2.addWidget(self.cNombreCliente)
        hbox2.addWidget(self.btnAgregarP)
        hbox2.addWidget(self.btnFinalizarP)
        
        main_layout.addWidget(self.pedidoLabel)
        main_layout.addLayout(hbox3)
        main_layout.addLayout(hbox)
        main_layout.addLayout(hbox1)
        main_layout.addLayout(hbox2)

        main = QWidget()
        main.setStyleSheet(self.pedidoSS)
        main.setLayout(main_layout)
        return main

    def ventanaInventario(self):
        self.tablaInventario = QTableWidget(2, 6)
        self.tablaInventario.setFixedSize(1260, 200)
        self.tablaInventario.setStyleSheet('border: none;')
        self.tablaInventario.setHorizontalHeaderLabels(['ID', 'Nombre del producto', 'Categoría', 'Ubicación', 'Cantidad', 'Costo unitario'])
        self.tablaInventario.setEditTriggers(QAbstractItemView.NoEditTriggers)
        

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.inventarioLabel)
        main_layout.addSpacerItem(QSpacerItem(10, 100))
        main_layout.addWidget(self.tablaInventario, Qt.AlignmentFlag.AlignCenter)
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main
        
    def ventanaVentas(self):
        self.tablaVentasDia = QTableWidget(self.filasVentasDia, 2)
        self.tablaVentasMes = QTableWidget(self.filasVentasMes, 2)
        self.tablaVentasDia.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaVentasMes.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaVentasDia.setHorizontalHeaderLabels(['Horas', 'Número de ventas'])
        self.tablaVentasMes.setHorizontalHeaderLabels(['Semana', 'Número de ventas'])
        self.tablaVentasDia.resizeColumnsToContents()
        self.tablaVentasMes.resizeColumnsToContents()
        self.tablaVentasDia.resizeRowsToContents()
        self.tablaVentasMes.resizeRowsToContents()

        for i in range(0, len(self.horas)):
            self.tablaVentasDia.setItem(i, 0, QTableWidgetItem(str(self.horas[i])))
            self.tablaVentasDia.setItem(i, 1, QTableWidgetItem(str(self.ventasH[i])))
            
        main_layout = QVBoxLayout()
        vbox = QVBoxLayout()
        vbox1 = QVBoxLayout()
        hbox = QHBoxLayout()

        vbox.addWidget(self.ventasDiaL)
        vbox.addWidget(self.tablaVentasDia)

        vbox1.addWidget(self.ventasMesL)
        vbox1.addWidget(self.tablaVentasMes)

        hbox.addLayout(vbox)
        hbox.addLayout(vbox1)

        main_layout.addWidget(self.ventasLabel)
        main_layout.addLayout(hbox)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ventanaAdminMatP(self):
        self.cT1.setEnabled(False)
        self.cT2.setEnabled(False)
        self.cT3.setEnabled(False)
        self.cT4.setEnabled(False)
        self.campoUsuarioMatP.setEnabled(False)
        self.campoContraseniaMatP.setEnabled(False)

        self.btnAceptar1.setEnabled(False)
        self.btnAceptar2.setEnabled(False)
        self.btnAutenticarMatP.setEnabled(False)

        self.materiaPrimaLabel.setText('Administración de Materia Prima')

        self.cT1.setStyleSheet("border: none;\nbackground-color: white;")
        self.cT2.setStyleSheet("border: none;\nbackground-color: white;")
        self.cT3.setStyleSheet("border: none;\nbackground-color: white;")
        self.cT4.setStyleSheet("border: none;\nbackground-color: white;")

        self.btnAgregar.setStyleSheet('border: 1px solid green;\nborder-radius: 5px;\nbackground-color: green;\ncolor: white;')
        self.btnEliminar.setStyleSheet('border: 1px solid red;\nborder-radius: 5px;\nbackground-color: red;\ncolor: white;')
        self.btnAceptar1.setStyleSheet('border: 1px solid white;\nborder-radius: 5px;\nbackground-color: white;\ncolor: white;')
        self.btnAceptar2.setStyleSheet('border: 1px solid white;\nborder-radius: 5px;\nbackground-color: white;\ncolor: white;')
        self.btnAutenticarMatP.setStyleSheet('border: 1px solid white;\nborder-radius: 5px;\nbackground-color: white;\ncolor: white;')

        self.btnAgregar.setFont(self.negrita14)
        self.btnEliminar.setFont(self.negrita14)
        self.btnAceptar1.setFont(self.negrita14)
        self.btnAceptar2. setFont(self.negrita14)
        self.btnAutenticarMatP.setFont(self.negrita14)
        
        self.tablaAMateriaPrima.setHorizontalHeaderLabels(['ID', 'Nombre', 'Categoría'])
        self.tablaAMateriaPrima.resizeRowsToContents()
        self.tablaAMateriaPrima.resizeColumnsToContents()
        self.tablaAMateriaPrima.setStyleSheet('border: none;')
        
        vbox = QVBoxLayout()
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        main_layout = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()

        vbox2.addWidget(self.campoUsuarioMatP)
        vbox2.addWidget(self.campoContraseniaMatP)
        vbox2.addWidget(self.btnAutenticarMatP)

        hbox3.addWidget(self.tablaAMateriaPrima)
        hbox3.addLayout(vbox2)

        hbox.addWidget(self.label2)
        hbox.addWidget(self.label3)
        hbox.addWidget(self.label4)

        hbox1.addWidget(self.cT1)
        hbox1.addWidget(self.cT2)
        hbox1.addWidget(self.cT3)

        vbox.addWidget(self.btnAgregar)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox1)
        vbox.addWidget(self.btnAceptar1)

        vbox1.addWidget(self.btnEliminar)
        vbox1.addWidget(self.label5)
        vbox1.addWidget(self.cT4)
        vbox1.addWidget(self.btnAceptar2)
        
        hbox2.addLayout(vbox)
        hbox2.addLayout(vbox1)

        main_layout.addWidget(self.materiaPrimaLabel)
        main_layout.addLayout(hbox3)
        main_layout.addLayout(hbox2)
        
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def administracionUsuarios(self):
        self.eliminarUsers.setStyleSheet('color: white;')
        self.modificarUser.setStyleSheet('color: white;')
        main_layout = QVBoxLayout()
        vbox = QVBoxLayout()
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        vbox3 = QVBoxLayout()
        vbox4 = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()

        vbox.addWidget(self.autenticarUsuariosLabel)
        vbox.addWidget(self.campoUsuario)
        vbox.addWidget(self.campoContrasenia)
        vbox.addWidget(self.btnIngresar)

        hbox.addWidget(self.tablaUsuarios)
        hbox.addLayout(vbox)

        vbox1.addWidget(self.btnAgregarUser, Qt.AlignmentFlag.AlignHCenter)
        vbox1.addWidget(self.campoNombreAgregar)
        vbox1.addWidget(self.campoUsuarioAgregar)
        vbox1.addWidget(self.campoContraseniaAgregar)
        vbox1.addWidget(self.campoTipoAgregar)
        vbox1.addWidget(self.btnEjecutarAgregar, Qt.AlignmentFlag.AlignHCenter)

        vbox2.addWidget(self.eliminarUsers)
        vbox2.addWidget(self.comboUsuario)
        vbox2.addWidget(self.btnEjecutarEliminar)

        hbox1.addWidget(self.comboCategoriaModificar)
        hbox1.addWidget(self.btnAceptarModificar)

        vbox3.addWidget(self.modificarUser)
        vbox3.addLayout(hbox1)
        vbox3.addWidget(self.comboOpcionesModificar)
        vbox3.addWidget(self.campoValorModificar)
        vbox3.addWidget(self.btnEjecutarModificar)

        hbox3.addLayout(vbox2)
        hbox3.addWidget(self.spacer)
        hbox3.addLayout(vbox3)
        
        vbox4.addWidget(self.btnEliminarUser)
        vbox4.addLayout(hbox3)

        hbox2.addLayout(vbox1)
        hbox2.addLayout(vbox4)

        main_layout.addWidget(self.adminUsuariosLabel)
        main_layout.addLayout(hbox)
        main_layout.addLayout(hbox2)
        main_layout.addWidget(self.confirmacionUsuariosLabel)
        main = QWidget()
        main.setStyleSheet(self.adminUsuariosSS)
        main.setLayout(main_layout)
        return main

    def administracionProductos(self):
        self.valoresTabla = back.Productos.valores(self)
        self.valoresCombo = back.Productos.valoresCombo(self)

        self.tablaAdminProductos = QTableWidget(len(self.valoresTabla), 2)
        self.tablaAdminProductos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaAdminProductos.setHorizontalHeaderLabels(['ID', 'Nombre'])

        self.labelAgregarP =  QLabel('Agregar')
        self.labelEliminarP = QLabel('Eliminar')

        self.campoUsuarioProductos.setEnabled(False)
        self.campoContraseniaProductos.setEnabled(False)
        self.btnIngresarAdminProd.setEnabled(False)
        self.campoIdProductos.setEnabled(False)
        self.campoNombreProductos.setEnabled(False)
        self.btnEjecutarAgregarP.setEnabled(False)
        self.campoIdProductosE.setEnabled(False)
        self.btnEjecutarEliminarP.setEnabled(False)

        self.labelAgregarP.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.spacer1.setFixedSize(100, 20)

        for i, val in enumerate(self.valoresTabla):
            self.tablaAdminProductos.setItem(i, 0, QTableWidgetItem(str(val[0])))
            self.tablaAdminProductos.setItem(i, 1, QTableWidgetItem(val[1]))

        self.tablaAdminProductos.setStyleSheet('border: none;')
        main_layout = QVBoxLayout()
        vbox = QVBoxLayout()
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox1 = QHBoxLayout()

        vbox.addWidget(self.lAutenticarUsuariosP)
        vbox.addWidget(self.campoUsuarioProductos)
        vbox.addWidget(self.campoContraseniaProductos)
        vbox.addWidget(self.btnIngresarAdminProd)

        hbox.addWidget(self.tablaAdminProductos)
        hbox.addLayout(vbox)

        vbox1.addWidget(self.labelAgregarP)
        vbox1.addWidget(self.campoIdProductos)
        vbox1.addWidget(self.campoNombreProductos)
        vbox1.addWidget(self.btnEjecutarAgregarP)

        vbox2.addWidget(self.labelEliminarP)
        vbox2.addWidget(self.campoIdProductosE)
        vbox2.addWidget(self.btnEjecutarEliminarP)

        hbox1.addLayout(vbox1)
        hbox1.addWidget(self.spacer1)
        hbox1.addLayout(vbox2)

        main_layout.addWidget(self.adminProductosLabel)
        main_layout.addLayout(hbox)
        main_layout.addWidget(self.btnDelAddProductos, Qt.AlignmentFlag.AlignVCenter)
        main_layout.addLayout(hbox1)
        main_layout.addWidget(self.lConfirmacionOperacionP)
        main = QWidget()
        main.setStyleSheet(self.adminProductosSS)
        main.setLayout(main_layout)
        return main


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    # Login = QMainWindow()
    # ui = Ui_Login()
    # ui.setupUi(Login)
    # Login.show()
    window.show()
    sys.exit(app.exec())
