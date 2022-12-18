import os
from time import time
import re
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
    def _init_(self, symbols):
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
            if self.Nodes[i].symbol == symbol and symbol != ' ':
                found = True
                index = i
                break
        if found:
            while index != -1:
                encoding = "%s%s" % (self.Nodes[index].encoding, encoding)
                index = self.Nodes[index].parent
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

if __name__=="__main__":
    print ("\n\n.....................CODIFICACIÓN DE HUFFMAN................\n\n")
    Names = []
    for line in open('Prueba.txt', 'r').readlines():
        Names.append(line.strip())
    print (Names)
    # simbolos=''
    # probabilidad=[]
    # msm="".join(Names)
    # msm=re.sub(r"\s+", "", msm)
    # msn2 = "".join(Names)
    # print ("\n\nTotal de simbolos: \n\n %s"% (len(msn2)))
    # name1 = "".join(Names)
    # name1 = re.sub(r"\s+", "", name1)
    # len_my_str = len(msm)
    # print('\nSu datos tienen una longitud de: ', len(msm), 'bytes')
    # d=0
    # longimed = 0
    # for i in name1:
    #     if i in msm:
    #             print (i,"=",int ( msm.count(i)))
    #             simbolos+=i
    #             probabilidad.append(float(float ( msm.count(i))/float(len(name1))))
    #             msm=msm.replace(i,'')
    #             d+= 1
                
    # symbols=dict(zip(simbolos, probabilidad))
    # print ("\n\nSimbolos comprimidos: \n\n",d)
    # print ("\n\nPROBABILIDAD DE CADA SIMBOLO:\n\n ", symbols)
    # tiempo_inicial= time()
    # list3 = []
    # huffman = Huffman(symbols)
    # print ("\n\nSimbolos codificados usando el arbol de Huffman: \n\n")   
    # for symbol in symbols:
    #     print ("Simbolo: %s; Codificando: %s" % (symbol, huffman.showSymbolEncoding(symbol)))
    #     list3.append(huffman.showSymbolEncoding(symbol))
    
    # for x,y in zip(list3, probabilidad):
    #     longimed = longimed + len(x)*y
        
    # encoded = huffman.encode(name1)
    # print ("\n\nMensaje que se esta codificando: \n\n%s" % (msn2))
    # print ("\n\nCodificacion en bits: \n\n%s" % (encoded))
    # print ("\n\nLa longitud de codigo binario es: \n\n%s" % (len(encoded)))
    # print("\nLongitud media = ", longimed,"\n")
    # data = encoded

    # fic = open("Prueba1.txt","w")
    # for line in data:
    #     fic.write(line)
    # fic.close();

    # compressed =  len(data)
    # original = len(msn2)
    # print("Compreso: ", compressed, "bytes\n")
    # print("Original: ", original, "bytes\n")
    # porcencompressed = 0
    # porcencompressed = (compressed/original)*100

    # print("\nPorcentaje de compresión = ", porcencompressed, "%")
    # tiempo_final= time()
    # tiempo_ejecucion= tiempo_final - tiempo_inicial
    # print ('\n\nEL tiempo de transmision es: ', tiempo_ejecucion)
os._exit(0)