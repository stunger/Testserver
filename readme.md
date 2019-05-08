## Custom Testserver setup

Dieser Server ist dafür gedacht Testfälle, die im Internet schwer zu finden sind zu
simulieren. Man kann dafür seine eigenen HTML Seiten schreiben und Header manipulieren.
Einige Dinge sind zu berücksichtigen:

+ Der Testserver läuft auf Port 8888 da der Scanner auf 8080 läuft. Zu Erreichen ist er also über 127.0.0.1:8888
+ Der Scanner verhindert Scans auf Localhost wenn man das nicht extra in utils.py auskommentiert.

```
denied_hosts = [
        # 'localhost' vor PUSH wieder zurücksetzen!
```

+ Das einzige verwendete Python Modul ist **bottlepy**. Kann installiert werden mit `sudo pip install bottle` oder `pip install -r requirements.txt`
+ Alternativ kann auch das vorhandene virtualenv verwendet werden: `source env/bin/activate`
+ Ausgeführt wird der Testserver mit `python test.py`
+ Beschreibungen zu Funktion im Quellcode und auf [bottlepy](https://bottlepy.org/docs/dev/tutorial.html)

## UPDATE

+ Testserver läuft nun auf Port 80 zur vereinfachung (muss beim scan nicht mehr angegeben werden)
+ trägt man einen alias in die /etc/hosts Datei ein (z.B. 127.0.0.1 www.test.at) muss keine Änderung an der utils.py vorgenommen werden