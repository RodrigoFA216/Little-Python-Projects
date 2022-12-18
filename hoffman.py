import os
from time import time

class Node:
    probability = 0.0
    symbol = ""
    encoding = ""
    visited = False 
    parent = -1

class Huffman: 
    Tree = None
    Root = None
    Nodes = []
    probs = {}
    dictEncoder = {}
    
    def __init__(self, symbols):
        self.initNodes(symbols)
        self.buildTree()
        self.buildDictionary()
        
    def initNodes(self, probs):
        for symbol in probs:
            node = Node()
            node.symbol = symbol
            node.probability = probs[symbol]
            node.visited = False
            self.Nodes.append(node)
            self.probs[symbol]=probs[symbol]
            
    def buildTree(self):
        indexMin1 = self.getNodeWithMinimumProb()
        indexMin2 = self.getNodeWithMinimumProb()
        
        while indexMin1 != -1 and indexMin2 != -1:
            node = Node()
            node.symbol = "."
            node.encoding = ""
            
            prob1 = self.Nodes[indexMin1].probability
            prob2 = self.Nodes[indexMin2].probability
            node.probability =prob1 + prob2
            node.visited = False
            node.parent = -1
            self.Nodes.append(node)
            self.Nodes[indexMin1].parent = len(self.Nodes) - 1
            self.Nodes[indexMin2].parent = len(self.Nodes) - 1
            
            if prob1 >= prob2:
                self.Nodes[indexMin1].encoding = "0"
                self.Nodes[indexMin2].encoding = "1"
                
            indexMin1 = self.getNodeWithMinimumProb()
            indexMin2 = self.getNodeWithMinimumProb()
            
    def getNodeWithMinimumProb(self):
        minProb = 1.0
        indexMin = -1
        
        for index in range(0, len(self.Nodes)):
            if (self.Nodes[index].probability < minProb and
                (not self.Nodes[index].visited)):
                minProb = self.Nodes[index].probability
                indexMin = index
                
        if indexMin != -1:
            self.Nodes[indexMin].visited = True
            
        return indexMin
    
    def showSymbolEncoding(self, symbol):
        found = False
        index = 0
        encoding = ""
        
        for i in range(0, len(self.Nodes)):
            if self.Nodes[i].symbol == symbol:
                found = True
                index = i
                break
            
        if found:
            while index != -1:
                encoding = "%s%s" % (self.Nodes[index].encoding, encoding)
                index = self.Nodes[index].parent
        else:
            encoding = "simbolo desconocido"
            
        return encoding
    
    def buildDictionary(self):
        for symbol in self.probs:
            encoding = self.showSymbolEncoding(symbol)
            self.dictEncoder[symbol] = encoding
            
    def encode(self, plain):
        encoded = ""
        for symbol in plain:
            encoded = "%s%s" % (encoded, self.dictEncoder[symbol])
            
        return encoded
    
    def decode(self, encoded):
        index = 0
        decoded = ""
        
        while index < len(encoded):
            found = False
            aux = encoded[index:]
            for symbol in self.probs:
                if aux.startswith(self.dictEncoder[symbol]):
                    decoded = "%s%s" % (decoded, symbol)
                    index = index + len(self.dictEncoder[symbol])
                    break
        return decoded


if __name__=="__main__":
    print ("........................................................................\n")
    print (".....................\t CODIFICACIÓN DE HUFFMAN \t................\n")
    print (".....................\t Integrantes del equipo \t................\n")
    print (".....................\t Flores Avalos Rodrigo Emmanuel ................\n")
    print (".....................\t Suarez Gonzales Edwin Deninson ................\n")
    print (".....................\t Rojano Peñaloza Eduardo \t................\n")
    print (".....................\t Gonzales Lavana Clara Abigail \t................\n")
    print (".....................\t Torres Chavez Henok \t\t................\n")
    print ("........................................................................\n")
    Names=[]
    with open('Prueba.txt','r') as archivo:
        lineas=archivo.readlines()
    # print(lineas)
    for line in lineas:
        x=line.count(" ")
        # print(x)
        y=line.replace(" ","",x)
        Names.append(y.strip("\n\t"))
    # print(Names)
    Result=""
    for line in Names:
        Result=Result+line
    # print(Result)
    mensaje=Result
    print ("\nla palabra que ingresaste fue: %s" %(mensaje))
    print ("\nTotal de simbolos: \n %s"% (len(mensaje)))
    simbolos=''
    probabilidad=[]
    msm=mensaje
    d=0
    for i in mensaje:
        if i in msm:
            simbolos+=i
            probabilidad.append(float(float ( msm.count(i))/float(len(mensaje))))
            msm=msm.replace(i,'')
            d+= 1
    symbols=dict(zip(simbolos, probabilidad))
    print ("\n\nSimbolos comprimidos: \n",d)
    print ("\n\nProbabilidad de cada simbolo:\n ", symbols)
    tiempo_inicial= time()
    huffman = Huffman(symbols)
    print ("\n\nSimbolos codificados usando el arbol de Huffman: \n")
    for symbol in symbols:
        print ("Simbolo: %s; Codificando: %s" % (symbol, huffman.showSymbolEncoding(symbol)))
    encoded = huffman.encode(mensaje)
    print ("\n\nMensaje que se esta codificando: \n%s" % (mensaje))
    print ("\n\nCodificacion en bits: \n%s" % (encoded))
    print ("\n\nLa longitud de codigo binario es: \n%s" % (len(encoded)))
    data = encoded
    # print ("\n\n.....................DEDIFICANDO................\n\n")
    # decoded = huffman.decode(data)
    # print ("El codigo binario a decodificar es: \n", data)
    # print ("\n\nEL mensaje decodificado es:\n%s" % (data))
    tiempo_final= time()
    tiempo_ejecucion= tiempo_final - tiempo_inicial
    print ('\n\nEL tiempo de transmision es: ', tiempo_ejecucion)
os._exit(0)