import mysql.connector

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


class Valores():
    def __init__(self):
        self._tipoCafe = []
        self._sabor = []
        self._tamanio = []
        self._tipoLeche = []
        self._extras = []
        self._tipoPedido = []
    
    def tipoCafe(self):
        self._tipoCafe = ['Frío', 'Caliente']
        return self._tipoCafe

    def sabor(self):
        self._sabor = ['    Cappuchino', '    Mocca']
        return self._sabor

    def tamanio(self):
        self._tamanio = ['    Chico', '    Mediano', '   Grande']
        return self._tamanio

    def tipoLeche(self):
        self._tipoLeche = ['    Entera', '    Deslactosada', '    Coco', '    Almendras']
        return self._tipoLeche

    def extras(self):
        self._extras = ['    cup holder']
        return self._extras

    def tipoPedido(self):
        self._tipoPedido = ['    Consumo Local', '    Para Llevar']
        return self._tipoPedido


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

        print(materiaP)


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
    

producto = Productos()
inventario = Inventario()

# inventario.valores()
