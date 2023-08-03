
## Rama feature creacion de la vista login

# creacion de carpetas

 - se creo las carpetas static y dentro de la carpeta css e img para guardar los archivos css e imagenes
 - tambien se creo la carpeta templates para crear los archivos html como el layout como principal utilizando bootstrap y una carpeta auth para crear la vista del login.

 # se creo la ruta en el archivo app.py 

  - Es decir, se creo la funcion login y en la funcion home el redireccionamient a la vista del login como se muestra en el codigo abajo

    ```
    
    #ruta al home
    @app.route("/")
    def home():
    return redirect(url_for("login"))
    
    #ruta al login
    @app.route("/login", methods=["GET" , "POST"])
    def login():
        if request.method == "POST":
            print(request.form['username'])
            print(request.form['password'])
            return render_template("auth/login.html")
        else:
            return render_template("auth/login.html")
    
```
