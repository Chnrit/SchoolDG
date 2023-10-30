from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/',methods=('GET', 'POST'))
def index():
   if request.method == "POST":
      list = []
      list.append(int(request.form.get('Korean')))
      list.append(int(request.form.get('Math')))
      list.append(int(request.form.get('English')))
      list.append(int(request.form.get('Soc')))
      list.append(int(request.form.get('His')))
      list.append(int(request.form.get('Sci')))

      dan = []
      dan.append(int(request.form.get('danKorean')))
      dan.append(int(request.form.get('danMath')))
      dan.append(int(request.form.get('danEnglish')))
      dan.append(int(request.form.get('danSoc')))
      dan.append(int(request.form.get('danHis')))
      dan.append(int(request.form.get('danSci')))

      total = list[0]*dan[0] + list[1]*dan[1] + list[2]*dan[2] + list[3]*dan[3] + list[4]*dan[4] + list[5]*dan[5]

      print(total)
      avg = int(total)/(sum(dan))
      roundedAvg = round(avg, 2)
      return render_template('index.html', list = list, roundedAvg = roundedAvg)
   elif request.method == "GET":
      list = []
      dan = [4, 4, 4, 4, 3, 4]
      for i in range(6):
         list.append('0')

      return render_template('index.html', list=list)

if __name__=="__main__":
   app.run(host="127.0.0.1", port="5000" , debug=True)