<h3 tabindex="-1" dir="auto">Проект по автоматизации тестирования Star Wars API и Google Maps API</h3>
<hr>
<h4 dir="auto"><em>В процессе тестов происходит:</em></h4>
<ul>
    <li>Проверка создания, изменения и удаления новой локации Google Maps API</li>
    <li>Сохранение имен всех персонажей, которые снимались в фильмах с Дарт Вейдером через Star Wars API, в текстовый файл </li>
</ul>
<hr>
<h4 dir="auto"><em>Для запуска тестов необходимо:</em></h4>
<ul>
     <li>Скачать проект с удаленного репозитория на свой локальный, с помощью команды:<br>     <code>git clone https://github.com/Aleks-QA/python_API_test.git</code></li>
     <li>Открыть проект на установленной заранее IDE</li>
</ul>  

<h5><em>Запуск тестов:</em></h5>
<ol>
     <li>Создать и активировать виртуальное окружение:<br><code>python -m venv venv</code><br>
     <code>venv\Scripts\activate</code></li>
     <li>Установить все зависимости: <br>          <code>python -m pip install -r requirements.txt</code> </li>
     <li>Запустить тесты командой:<br><code>python -s -m pytest --alluredir=test_results</code> </li>
     <li>Открыть отчет о прохождении тестов командой:<br>          <code>allure serve test_results/ </code></li>
</ol>

<h5><em>Запуск тестов в Docker:</em></h5>
<ol>
    <li>Развернуть контейнер с помощью команды:<br><code>docker-compose up --build</code></li>
    <li>Открыть отчет о прохождении тестов командой:<br>          <code>allure serve test_results/ </code></li>
</ol>
