from flask import request,render_template
from model import db,Submissions,select
from database import app

@app.route("/",methods = ["GET","POST"])
def selectPyramids():
  if request.method == "POST":
     name = request.form.get("name")
     try:
        height = int(request.form.get("height"))
        if 1 <= height <= 8:
           pyramid = get_pyramid(height)
           sub = Submissions(
              name = name,
              height = height,
              pyramid = pyramid
           )
           db.session.add(sub)
           db.session.commit()
           return render_template("index.html", submissions=pyramidList())
        else:
           error = "Height must be a number between 1 and 8."
           return render_template("index.html",error = error,submissions = pyramidList())
     except ValueError:
        error = "Invalid input. Please enter a valid number."
        return render_template("index.html",error = error,submissions = pyramidList())
  else:
       print(pyramidList())
       return render_template("index.html", submissions=pyramidList())



def get_pyramid(height):
   pyramid = []
   for i in range(1, height + 1):
        spaces = " " * (height - i)
        hashes = "#" * i
        pyramid.append(f"{spaces}{hashes}  {hashes}")
   return "<br>".join(pyramid)
      

def pyramidList():
   result =  db.session.scalars(select(Submissions).order_by(Submissions.id.desc())).all()
   return [(s.name, s.height, s.pyramid) for s in result]
   

if __name__ == "__main__":
    app.run(debug=True)