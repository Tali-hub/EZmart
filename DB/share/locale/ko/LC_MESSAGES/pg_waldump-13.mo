Þ    4      ¼  G   \      x  
   y  3     %   ¸  3   Þ  ?     I   R  =     A   Ú  6     ç   S     ;  >   Ù       C     ~   â  D   a	     ¦	  &   Æ	     í	  Ü   õ	  )   Ò
     ü
          5  !   T     v       (   ¬  %   Õ     û  '        >     \  (   y  9   ¢  :   Ü  .     .   F      u            |   ¦     #     :     V  !   d  $     0   «  /   Ü  $     	   1  {  ;     ·  2   Ä  /   ÷  >   '  ;   f  O   ¢  ?   ò  I   2  1   |  ô   ®  ¡   £  ?   E       >        L  Z   Õ  &   0  A   W          ¥  1   3  &   e  $        ±  '   Ï     ÷  !     9   7  1   q  #   £  '   Ç  0   ï  $      7   E  P   }  L   Î  @     -   \  +        ¶     ¿  G   È       /   *     Z  !   k  ,     0   º  C   ë  )   /     Y            -                      .   %                   *      $   "          2                  	   0   &   !          '               3      1          #      +       (      )                  /                                
          4      ,        
Options:
 
Report bugs to <pgsql-bugs@lists.postgresql.org>.
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
   -r, --rmgr=RMGR        only show records generated by resource manager RMGR;
                         use --rmgr=list to list valid resource manager names
   -s, --start=RECPTR     start reading at WAL location RECPTR
   -t, --timeline=TLI     timeline from which to read log records
                         (default: 1 or the value used in STARTSEG)
   -x, --xid=XID          only show records with transaction ID XID
   -z, --stats[=record]   show statistics instead of records
                         (optionally, show per-record statistics)
 %s decodes and displays PostgreSQL write-ahead logs for debugging.

 ENDSEG %s is before STARTSEG %s Try "%s --help" for more information.
 Usage:
 WAL segment size must be a power of two between 1 MB and 1 GB, but the WAL file "%s" header specifies %d byte WAL segment size must be a power of two between 1 MB and 1 GB, but the WAL file "%s" header specifies %d bytes could not find a valid record after %X/%X could not find any WAL file could not find file "%s": %s could not locate WAL file "%s" could not open directory "%s": %s could not open file "%s" could not open file "%s": %s could not parse "%s" as a transaction ID could not parse end WAL location "%s" could not parse limit "%s" could not parse start WAL location "%s" could not parse timeline "%s" could not read file "%s": %s could not read file "%s": read %d of %zu could not read from log file %s, offset %u, length %d: %s could not read from log file %s, offset %u: read %d of %zu could not seek in log file %s to offset %u: %s end WAL location %X/%X is not inside file "%s" error in WAL record at %X/%X: %s error:  fatal:  first record is after %X/%X, at %X/%X, skipping over %u byte
 first record is after %X/%X, at %X/%X, skipping over %u bytes
 no arguments specified no start WAL location given out of memory path "%s" could not be opened: %s resource manager "%s" does not exist start WAL location %X/%X is not inside file "%s" too many command-line arguments (first is "%s") unrecognized argument to --stats: %s warning:  Project-Id-Version: pg_waldump (PostgreSQL) 12
Report-Msgid-Bugs-To: pgsql-bugs@lists.postgresql.org
PO-Revision-Date: 2019-10-31 18:06+0900
Last-Translator: Ioseph Kim <ioseph@uri.sarang.net>
Language-Team: Korean <pgsql-kr@postgresql.kr>
Language: ko
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Plural-Forms: nplurals=1; plural=0;
 
ìµìë¤:
 
ì¤ë¥ë³´ê³ : <pgsql-bugs@lists.postgresql.org>.
   %s [ìµì]... [ììíì¼ [ë§ì¹¨íì¼]]
   -?, --help             ì´ ëìë§ì ë³´ì¬ì£¼ê³  ë§ì¹¨
   -V, --version          ë²ì  ì ë³´ ë³´ì¬ì£¼ê³  ë§ì¹¨
   -b, --bkp-details      ë°±ì ë¸ë¡ì ëí ìì¸í ì ë³´ë ì¶ë ¥í¨
   -e, --end=RECPTR       RECPTR WAL ìì¹ìì ì½ê¸° ë©ì¶¤
   -f, --follow           WAL ëê¹ì§ ì½ì ë¤ìë ê³ì ì§íí¨
   -n, --limit=N          ì¶ë ¥í  ë ì½ë ì
   -p, --path=PATH        ë¡ê·¸ ì¡°ê° íì¼ì´ ìë ëë í°ë¦¬ ì§ì , ëë
                         ./pg_wal ëë í°ë¦¬ê° ìë ëë í°ë¦¬ ì§ì 
                         (ê¸°ë³¸ê°: íì¬ ëë í°ë¦¬, ./pg_wal, PGDATA/pg_wal)
   -r, --rmgr=RMGR        ë¦¬ìì¤ ê´ë¦¬ì RMGRìì ë§ë  ë ì½ëë§ ì¶ë ¥í¨
                         ë¦¬ìì¤ ê´ë¦¬ì ì´ë¤ì --rmgr=list ë¡ ë´
   -s, --start=RECPTR     WAL RECPTR ìì¹ìì ì½ê¸° ìì
   -t, --timeline=TLI     ì½ê¸° ììí  íìë¼ì¸ ë²í¸
                         (ê¸°ë³¸ê°: 1 ëë STARTSEGì ì¬ì©ë ê°)
   -x, --xid=XID          í¸ëì­ì XID ë ì½ëë§ ì¶ë ¥
   -z, --stats[=record]   ë í¬ë íµê³ ì ë³´ë¥¼ ë³´ì¬ì¤
                         (ì¶ê°ë¡, ë ì½ëë¹ íµê³ì ë³´ë¥¼ ì¶ë ¥)
 %s ëªë ¹ì ëë²ê¹ì ìí´ PostgreSQL ë¯¸ë¦¬ ì°ê¸° ë¡ê·¸(WAL)ë¥¼ ë¶ìí©ëë¤.
 %s ENDSEGê° %s STARTSEG ìì ìì ìì í ì¬í­ì "%s --help" ëªë ¹ì¼ë¡ ì´í´ë³´ì­ìì¤.
 ì¬ì©ë²:
 WAL ì¡°ê° íì¼ í¬ê¸°ë 1MBìì 1GBì¬ì´ 2^n ì´ì´ì¼íì§ë§, "%s" WAL íì¼ í¤ëìë %d ë°ì´í¸ë¡ ì§ì ëì´ììµëë¤ %X/%X ìì¹ ë¤ì ì¬ë°ë¥¸ ë ì½ëê° ìì ì´ë¤ WAL íì¼ë ì°¾ì ì ìì "%s" íì¼ì ì°¾ì ì ìì: %s "%s" WAL íì¼ ì°¾ê¸° ì¤í¨ "%s" ëë í°ë¦¬ë¥¼ ì´ ì ìì: %s "%s" íì¼ì ì´ ì ìì "%s" íì¼ì ì´ ì ìì: %s "%s" ë¬¸ìì´ì í¸ëì­ì IDë¡ í´ìí  ì ìì "%s" ì´ë¦ì WAL ìì¹ë¥¼ í´ìí  ì ìì "%s" ì íì í´ìí  ì ìì "%s" WAL ìì¹ë¥¼ í´ìí  ì ìì "%s" íìë¼ì¸ ë²í¸ë¥¼ í´ìí  ì ìì "%s" íì¼ì ì½ì ì ìì: %s "%s" íì¼ì ì½ì ì ìì: %d ì½ì, ì ì²´ %zu %s ë¡ê·¸ ì¡°ê° íì¼ìì %u ìì¹ìì %d ê¸¸ì´ë¥¼ ì½ì ì ìì: %s %s ë¡ê·¸ ì¡°ê° íì¼ìì %u ìì¹ìì ì½ê¸° ì¤í¨: %d / %zu ì½ì %s ë¡ê·¸ ì¡°ê° íì¼ìì %u ìì¹ë¥¼ ì°¾ì ì ìì: %s %X/%X WAL ë ìì¹ê° "%s" íì¼ì ìì %X/%X ìì¹ìì WAL ë ì½ë ì¤ë¥: %s ì¤ë¥:  ì¬ê°:  ì²« ë ì½ëê° %X/%X ë¤ì ìê³ , (%X/%X), %u ë°ì´í¸ ê±´ë ë
 ì¸ìë¥¼ ì§ì íì¸ì ìë ¥í WAL ìì¹ìì ììí  ì ìì ë©ëª¨ë¦¬ ë¶ì¡± "%s" ê²½ë¡ë¥¼ ì´ ì ìì: %s "%s" ì´ë¦ì ë¦¬ìì¤ ê´ë¦¬ìê° ìì %X/%X WAL ìì ìì¹ê° "%s" íì¼ì ìì ëë¬´ ë§ì ëªë ¹í ì¸ìë¥¼ ì§ì íìµëë¤. (ì²ì "%s") --stats ìµìê°ì´ ë°ë¥´ì§ ìì: %s ê²½ê³ :  