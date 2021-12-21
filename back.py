import mysql.connector
import calendar
from datetime import date

class Autenticacion():
    def __init__(self) -> None:
        pass

    def autenticar(self, usuario, contrasenia):
        conexion = mysql.connector.connect( host='localhost', database ='CafeteriaDB', 
                                                user = 'root',password ='admin')
        cursr = conexion.cursor()
        cursr.execute("SELECT * FROM empleados")
        empleadosInfo = cursr.fetchall()
        cursr.close()

        dictCredenciales = dict()
        self.autenticacion = False
        self.administrador = False

        for i in empleadosInfo:
            if usuario in i and i[6] == 'gerente':
                self.administrador = True
            dictCredenciales[i[7]] = i[8]
        
        if usuario in dictCredenciales and contrasenia == dictCredenciales[usuario]:
            self.autenticacion = True

        return self.autenticacion, self.administrador


class Pedidos():
    def __init__(self):
        pass

    def valores(self):
        conexion = mysql.connector.connect( host='localhost', database ='CafeteriaDB', 
                                            user = 'root', password ='admin')

        cursorPedidos = conexion.cursor()
        cursorPedidos.execute('SELECT tipoBebida, sabor, tamaño, tipoLeche, extra0, tipoConsumo FROM pedidos')
        valPedido = cursorPedidos.fetchall()
        cursorPedidos.close()

        tipoCafe = []
        flavour = dict()
        tamanio = []
        tipoLeche = []
        extras = []
        tipoPedido = []
        sabores = []
        sabores = []
        tamanioDict = {'ch': 'Chico',
                        'g': 'Grande',
                        'm': 'Mediano'}
        lecheDict = {'alm': 'Almendras',
                    'enter': 'Entera',
                    'des': 'Deslactosada'}
        pedidoDict = {'loc': 'Local',
                    'nloc': 'Para llevar'}
        tam = valPedido[0][2].split('-')
        leche = valPedido[0][3].split('-')
        pedido = valPedido[0][5].split('-')

        tuplaSabor = []
        listaSabor = []
        for i in valPedido:
            cafe = i[0]
            sabor = i[1]
            extra = i[4]
            

            if cafe in flavour:
                listaSabor = list(flavour[cafe])
            
            listaSabor.append(sabor)
            tuplaSabor = tuple(listaSabor)
            flavour[cafe] = tuplaSabor

            listaSabor.clear()

            if cafe not in tipoCafe:
                tipoCafe.append(cafe)

            if extra not in extras:
                extras.append(extra)
        
        for i in tam:
            tamanio.append(tamanioDict[i])
        
        for i in leche:
            tipoLeche.append(lecheDict[i])
        
        for i in pedido:
            tipoPedido.append(pedidoDict[i])

        sabores = []


        for key, val in flavour.items():
            sabores.append(key)
            for i1 in val:
                sabores.append(i1)

        return tipoCafe, sabores, tamanio, tipoLeche, extras, tipoPedido
        

class Ventas():
    def __init__(self):
        self._horas = []
        self._ventasH = []
        self._semanas = []
        self._ventasM = []

    def ventasD(self):
        self._horas = [ 13 , 14, 16]
        self._ventasH = [3, 2, 4]
        
        return self._horas, self._ventasH

    def ventasM(self):
        self._semanas = [1, 2, 3, 4]
        self._ventasM = [12, 20, 10, 5]

        return self._semanas, self._ventasM


class Login():
    def __init__(self):
        self.conexion = mysql.connector.connect( host='localhost',
                                            database ='CafeteriaDB', 
                                            user = 'root',
                                            password ='admin')

    def busca_users(self, users):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM empleados WHERE users = {}".format(users)
        cur.execute(sql)
        usersx = cur.fetchall()
        cur.close()     
        return usersx 

    def busca_password(self, password):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM empleados WHERE Password = {}".format(password) #
        cur.execute(sql)
        passwordx = cur.fetchall()
        cur.close()     
        return passwordx 


class AdminUsers():
    def __init__(self):
        pass


class Inventario():
    def __init_(self):
        pass

    def valores(self):
        conexion = mysql.connector.connect( host='localhost',
                                            database ='cafeteriaDB', 
                                            user = 'root',
                                            password ='admin')

        miCursor = conexion.cursor()
        miCursor.execute('SELECT * FROM empleados')
        materiaP = miCursor.fetchall()
        miCursor.close()


class Productos():
    def __init__(self):
        pass
        

    def credenciales(self, usuario, contrasenia):
        conexion = mysql.connector.connect( host='localhost', database ='CafeteriaDB', 
                                                user = 'root',password ='admin')
        cursr = conexion.cursor()
        cursr.execute("SELECT * FROM empleados")
        empleadosInfo = cursr.fetchall()
        cursr.close()

        dictCredenciales = dict()
        self.autenticacion = False
        self.administrador = False

        for i in empleadosInfo:
            if usuario in i and i[6] == 'gerente':
                self.administrador = True
            dictCredenciales[i[7]] = i[8]
        
        if usuario in dictCredenciales and contrasenia == dictCredenciales[usuario]:
            self.autenticacion = True

        return self.autenticacion, self.administrador

    def valores(self):
        conexion =  mysql.connector.connect( host='localhost',
                                            database ='CafeteriaDB', 
                                            user = 'root',
                                            password ='admin')
        curs = conexion.cursor()
        curs.execute('SELECT idPedido, tipoBebida, sabor FROM pedidos')
        valoresTablaP = curs.fetchall()
        curs.close()

        listaTemp = []
        listaFinal = []

        for i in valoresTablaP:
            tipoSabores = i[1] + ' ' + i[2]
            listaTemp.append(i[0])
            listaTemp.append(tipoSabores)
            listaFinal.append(tuple(listaTemp))
            listaTemp = []

        return listaFinal

    def valoresCombo(self):
        conexion =  mysql.connector.connect( host='localhost',
                                            database ='CafeteriaDB', 
                                            user = 'root',
                                            password ='admin')
        curs = conexion.cursor()
        curs.execute('SELECT idPedido FROM pedidos')
        comboId = curs.fetchall()
        curs.close()
        valoresComboId = []
        
        for i in comboId:
            valoresComboId.append(str(i[0]))

        return valoresComboId

    def agregarP(self, id1, nombre):
        nombre = nombre.split()
        agrega = f"INSERT INTO `cafeteriadb`.`pedidos` (`idPedido`, `tipoBebida`, `sabor`, `tamaño`, `tipoLeche`, `extra0`, `extra1`, `extra2`, `extra3`, `extra4`, `cantidad`, `tipoConsumo`, `nombre`) VALUES ('{id1}', '{nombre[0]}', '{nombre[1]}', 'chico-mediano-grande', 'alm-ent-des', 'no', 'no', 'no', 'no', 'no', '0', 'loc-nLoc', 'no');"
        conexion =  mysql.connector.connect( host='localhost', database ='CafeteriaDB', 
                                            user = 'root', password ='admin')
        curs = conexion.cursor()
        curs.execute(agrega)
        conexion.commit()
        curs.close()

    def eliminarP(self, id1):
        elimina = f"DELETE FROM pedidos WHERE idPedido = {id1}"
        conexion =  mysql.connector.connect( host='localhost', database ='CafeteriaDB', 
                                            user = 'root', password ='admin')
        curs = conexion.cursor()
        curs.execute(elimina)
        conexion.commit()
        curs.close()

class AdminMatP():
    def __init__(self) -> None:
        pass

    def valores(self):
        conexion =  mysql.connector.connect( host='localhost', database ='CafeteriaDB', 
                                            user = 'root', password ='admin')
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM materiaprima')
        materiaPrima = cursor.fetchall()
        cursor.close()
    
        return materiaPrima
    
    def agregarMatP(self, idMP, nombreMP, categoriaMP):
        agregar = f"INSERT INTO `cafeteriadb`.`materiaprima` (`idMatPrima`, `nomMatPrima`, `categoria`) VALUES ('{idMP}', '{nombreMP}', '{categoriaMP}');"
        conexion =  mysql.connector.connect( host='localhost', database ='CafeteriaDB', 
                                            user = 'root', password ='admin')
        cursorAdd = conexion.cursor()
        cursorAdd.execute(agregar)
        conexion.commit()
        cursorAdd.close()

    def eliminarMatP(self, idEliminar):
        eliminaId = f"DELETE FROM materiaprima WHERE idMatPrima = {idEliminar}"
        conexion =  mysql.connector.connect( host='localhost', database ='CafeteriaDB', 
                                            user = 'root', password ='admin')
        curs = conexion.cursor()
        curs.execute(eliminaId)
        conexion.commit()
        curs.close()


class Vent():
    def __init__(self) -> None:
        pass

    def valoresMes(self):
        conexion =  mysql.connector.connect( host='localhost', database ='CafeteriaDB', 
                                            user = 'root', password ='admin')
        cursor = conexion.cursor()
        cursor.execute('SELECT montoTotal, fecha FROM reportesventas')
        valMes = cursor.fetchall()
        cursor.close()

        fecha = date.today()
        noFilas = len(calendar.monthcalendar(2021, fecha.month))

        listaTemp = []
        listaFinal = []
        listaFecha = []

        for i, val in enumerate(valMes):
            lol = val[1].split()
            listaTemp.append(val[0])
            listaFecha = lol[0].split('-')
            for j in listaFecha:
                listaTemp.append(j)
            listaTemp.append(lol[1])
            listaFinal.append(tuple(listaTemp))
            listaTemp.clear()

        return noFilas


producto = Productos()
inventario = Inventario()
ventas = Vent()
val = Pedidos()

