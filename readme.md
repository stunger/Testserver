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
+ Ausgeführt wird der Testserver mit `python test.py`
+ Beschreibungen zu Funktion im Quellcode und auf [bottlepy](https://bottlepy.org/docs/dev/tutorial.html)

## UPDATE

+ Testserver Port kann nun beim start angegben werden (usage: test.py [-h] [-p PORT])
+ Port 80 benötigt Root-Rechte
+ trägt man einen alias in die /etc/hosts Datei ein (z.B. 127.0.0.1 www.test.at) muss keine Änderung an der utils.py vorgenommen werden