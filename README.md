# Django-React-Notes-App
Projeto criado para estudo e aprimoramento das tecnologias React-Django-Postgres juntas, projeto fullstack baseado em APIS e de referemcia no projeto do instrutor Dennys Ivy (https://www.youtube.com/watch?v=tYKRAXIio28).

## Arquitetura do projeto: 
![MVT (1)](https://github.com/eliascastrosousa/Django-React-Notes-App/assets/73971067/bf5300da-3687-4c23-8e79-90c58aeab92a)

## Ao Clonar o projeto é necessario ter instalado o PGAdmin 4 para utilizar o banco configurado, ou trocar nas settings as configurações para sqlite.

~~~powershell
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
~~~
### Back-end Django
~~~powershell
  python -m venv env
~~~
~~~powershell
  .\env\scripts\activate
~~~
~~~powershell
  pip install -r requirements.txt

~~~
~~~powershell
  python manage.py migrate
~~~
~~~powershell
  python manage.py runserver
~~~

### Front-end React

#### Necessario ter instalado o Node.js e React framework

~~~powershell
 cd .\front-end\
~~~
~~~powershell
 npm start
~~~



https://github.com/eliascastrosousa/Django-React-Notes-App/assets/73971067/bc188ede-26bd-4074-bf8f-408fc08f2003

![image](https://github.com/eliascastrosousa/Django-React-Notes-App/assets/73971067/bf8ac31f-510a-45be-bc80-b9e01ffd886c)

![image](https://github.com/eliascastrosousa/Django-React-Notes-App/assets/73971067/b3a2ccda-02fa-4f5f-813b-600ce594e42e)

![image](https://github.com/eliascastrosousa/Django-React-Notes-App/assets/73971067/78e3af45-5ba9-46f4-b5a9-94cd3668d1c3)

![image](https://github.com/eliascastrosousa/Django-React-Notes-App/assets/73971067/98aae6da-237a-46b6-ad1d-d55512bf5cd8)

