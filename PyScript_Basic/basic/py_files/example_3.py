import js
from js import document

def main():
  msg = document.getElementById("msg")
  msg.innerHTML = 'Pyodide 사용 예제'

main()