#!/usr/bin/python

from BeautifulSoup import BeautifulSoup
import urllib2

url = 'http://investigacion.ugr.es/ugrinvestiga/static/BuscadorRanking/*/buscar?tipo=&rama_c=&disciplina_c=TELE_D&especialidad_c=&indicador=&periodo='
response = urllib2.urlopen( url )
html= response.read()
all_data = BeautifulSoup( html )
investigadores = all_data.find( "table" ).findAll( "tr" )

for row in investigadores[1:]:
    columnas = row.findAll('td')
    rank =  int(columnas[0].string.strip())
    nombre =  columnas[1].find('a').string.strip()
    citas =  int(columnas[2].find('strong').string.strip())
    h =  int(columnas[3].string.strip())
    print rank, " - " , nombre, " - ", citas, " - ", h
    
    
