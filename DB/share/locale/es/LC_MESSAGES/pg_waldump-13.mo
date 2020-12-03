��    4      �  G   \      x  
   y     �  %   �  3   �  ?   �  I   5  =     A   �  6   �  �   6  D     �   c  >     �   @  C   �  ~   
	  D   �	     �	     �	  &   
     )
  �   1
  )        8     T     q  !   �     �     �  (   �  %        7  '   R     z     �  (   �  *   �  6   	  .   @      o     �     �  |   �          4     P  $   ^  0   �  /   �  $   �  	   	  �       �     �  *   �  ;     I   Y  T   �  M   �  U   F  :   �    �  K   �  �   %  H   �  �     Q   �  �   �  J   �     �  )   �  .        L    U  :   b  (   �  *   �  '   �  )     "   C  &   f  8   �  7   �  (   �  9   '  )   a  %   �  4   �  >   �  ?   %  =   e  %   �     �     �  �   �  #   �  *   �     �  &   �  ?     E   F  )   �     �            /       &       $         '                   +          .          2   -      4       	           #          (                       1          %      ,       )      *   3   "           0       !                         
                        
Options:
 
Report bugs to <%s>.
   %s [OPTION]... [STARTSEG [ENDSEG]]
   -?, --help             show this help, then exit
   -V, --version          output version information, then exit
   -b, --bkp-details      output detailed information about backup blocks
   -e, --end=RECPTR       stop reading at WAL location RECPTR
   -f, --follow           keep retrying after reaching end of WAL
   -n, --limit=N          number of records to display
   -p, --path=PATH        directory in which to find log segment files or a
                         directory with a ./pg_wal that contains such files
                         (default: current directory, ./pg_wal, $PGDATA/pg_wal)
   -q, --quiet            do not print any output, except for errors
   -r, --rmgr=RMGR        only show records generated by resource manager RMGR;
                         use --rmgr=list to list valid resource manager names
   -s, --start=RECPTR     start reading at WAL location RECPTR
   -t, --timeline=TLI     timeline from which to read log records
                         (default: 1 or the value used in STARTSEG)
   -x, --xid=XID          only show records with transaction ID XID
   -z, --stats[=record]   show statistics instead of records
                         (optionally, show per-record statistics)
 %s decodes and displays PostgreSQL write-ahead logs for debugging.

 %s home page: <%s>
 ENDSEG %s is before STARTSEG %s Try "%s --help" for more information.
 Usage:
 WAL segment size must be a power of two between 1 MB and 1 GB, but the WAL file "%s" header specifies %d byte WAL segment size must be a power of two between 1 MB and 1 GB, but the WAL file "%s" header specifies %d bytes could not find a valid record after %X/%X could not find any WAL file could not find file "%s": %m could not locate WAL file "%s" could not open directory "%s": %m could not open file "%s" could not open file "%s": %m could not parse "%s" as a transaction ID could not parse end WAL location "%s" could not parse limit "%s" could not parse start WAL location "%s" could not parse timeline "%s" could not read file "%s": %m could not read file "%s": read %d of %zu could not read from file %s, offset %u: %m could not read from file %s, offset %u: read %d of %zu end WAL location %X/%X is not inside file "%s" error in WAL record at %X/%X: %s error:  fatal:  first record is after %X/%X, at %X/%X, skipping over %u byte
 first record is after %X/%X, at %X/%X, skipping over %u bytes
 no arguments specified no start WAL location given out of memory resource manager "%s" does not exist start WAL location %X/%X is not inside file "%s" too many command-line arguments (first is "%s") unrecognized argument to --stats: %s warning:  Project-Id-Version: pg_waldump (PostgreSQL) 12
Report-Msgid-Bugs-To: pgsql-bugs@lists.postgresql.org
PO-Revision-Date: 2020-09-18 18:35-0300
Last-Translator: Carlos Chapi <carlos.chapi@2ndquadrant.com>
Language-Team: PgSQL-es-Ayuda <pgsql-es-ayuda@lists.postgresql.org>
Language: es
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
X-Generator: Poedit 2.0.2
Plural-Forms: nplurals=2; plural=n != 1;
 
Opciones:
 
Reporte errores a <%s>.
   %s [OPCIÓN]... [SEGINICIAL [SEGFINAL]]
   -?, --help               mostrar esta ayuda, luego salir
   -V, --version            mostrar información de versión, luego salir
   -b, --bkp-details        mostrar información detallada sobre bloques de respaldo
   -e, --end=RECPTR         detener la lectura del WAL en la posición RECPTR
   -f, --follow             seguir reintentando después de alcanzar el final del WAL
   -n, --limit=N            número de registros a mostrar
   -p, --path=RUTA          directorio donde buscar los archivos de segmento de WAL
                           o un directorio con un ./pg_wal que contenga tales archivos
                           (por omisión: directorio actual, ./pg_wal, $PGDATA/pg_wal)
   -q, --quiet                 no escribir ningún mensaje, excepto errores
   -r, --rmgr=GREC          sólo mostrar registros generados por el gestor de
                           recursos GREC; use --rmgr=list para listar nombres válidos
   -s, --start=RECPTR       empezar a leer el WAL en la posición RECPTR
   -t, --timeline=TLI       timeline del cual leer los registros de WAL
                           (por omisión: 1 o el valor usado en SEGINICIAL)
   -x, --xid=XID            sólo mostrar registros con el id de transacción XID
   -z, --stats[=registro]   mostrar estadísticas en lugar de registros
                           (opcionalmente, mostrar estadísticas por registro)
 %s decodifica y muestra segmentos de WAL de PostgreSQL para depuración.

 Sitio web de %s: <%s>
 SEGFINAL %s está antes del SEGINICIAL %s Pruebe «%s --help» para mayor información.
 Empleo:
 el tamaño de segmento WAL debe ser una potencia de dos entre 1 MB y 1 GB, pero la cabecera del archivo WAL «%s» especifica %d byte el tamaño de segmento WAL debe ser una potencia de dos entre 1 MB y 1 GB, pero la cabecera del archivo WAL «%s» especifica %d bytes no se pudo encontrar un registro válido después de %X/%X no se pudo encontrar ningún archivo WAL no se pudo encontrar el archivo «%s»: %m no se pudo ubicar el archivo WAL «%s» no se pudo abrir el directorio «%s»: %m no se pudo abrir el archivo «%s» no se pudo abrir el archivo «%s»: %m no se pudo interpretar «%s» como un id de transacción no se pudo interpretar la posición final de WAL «%s» no se pudo interpretar el límite «%s» no se pudo interpretar la posición inicial de WAL «%s» no se pudo interpretar el timeline «%s» no se pudo leer el archivo «%s»: %m no se pudo leer el archivo «%s»: leídos %d de %zu no se pudo leer desde el archivo «%s» en la posición %u: %m no se pudo leer del archivo %s, posición %u: leídos %d de %zu la posición final de WAL %X/%X no está en el archivo «%s» error en registro de WAL en %X/%X: %s error:  fatal:  el primer registro está ubicado después de %X/%X, en %X/%X, saltándose %u byte
 el primer registro está ubicado después de %X/%X, en %X/%X, saltándose %u bytes
 no se especificó ningún argumento no se especificó posición inicial de WAL memoria agotada el gestor de recursos «%s» no existe la posición inicial de WAL %X/%X no está en el archivo «%s» demasiados argumentos en la línea de órdenes (el primero es «%s») parámetro no reconocido para --stats: %s precaución:  