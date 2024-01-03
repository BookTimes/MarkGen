import plotly.graph_objects as go
from string import Template




while True:
    subject = []
    categories = []
    submark = ()
    topmark = ()
    avmark = ()
    print("\033[36mMarklist Generation Software\033[0m \n\tHOME")
    t = '2'
    if t == "1" :
        print("""HELP DOCUMENTATION
        \t Marks can be entered in format [\033[95m SCORED MARKS/TOTAL MARK\033[0m]""")
    elif t == "2":
        student_name = "mahadev"
        gr_number = '040963'
        while len(gr_number) != 6:
            print("Format not correct")
            gr_number = input("Enter GR number of the student: ")
        ClassAndSection = '11 c'
        while " " not in ClassAndSection:
            print("Format not correct")
            ClassAndSection = input("Enter Class and Section of the student separated by a space: ")
        ClassAndSection = ClassAndSection.split(" ")
        Class = ClassAndSection[0]
        section = ClassAndSection[1]
        gaurdianName = 'Maneesh'
        remarks = "Nothing official about it aha"
        disci = int('5')
        s = 'Physics,Maths,Computer Science,Typography,Arabic'
        s = s.split(",")
        print("Marks can be entered in format [\033[95m SCORED MARKS/TOTAL MARK\033[0m]")
        w = 7
        for sub in s:
            mark = f'{w}/25'
            itrnl = '10/10'
            cltp = '10/25'
            clav = '8/25'
            temp = mark
            w +=1
            mark = eval(mark) * 100
            if mark >= 91 and mark <= 100:
                grade = 'A1'
            elif mark >= 81 and mark <= 90:
                grade = 'A2'
            elif mark >= 71 and mark <= 80:
                grade = 'B1'
            elif mark >= 61 and mark <= 70:
                grade = 'B2'
            elif mark >= 51 and mark <= 60:
                grade = 'C1'
            elif mark >= 41 and mark <= 50:
                grade = 'C2'
            elif mark >= 33 and mark <= 40:
                grade = 'D'
            elif mark >= 0 and mark <= 32:
                grade = 'E'
            else :
                grade = 'Fail'


            subject.append({"sub" : sub , "mark" : temp.split('/') , "internal":itrnl.split('/') , "classav" : clav.split('/') , "classtop":cltp.split('/') , 'grade' : grade , 'totmark' : eval(itrnl) + mark})
            submark += (eval(temp),)
            topmark += (eval(cltp),)
            avmark += (eval(clav),)
            if sum(submark) - sum(avmark) < 0 :
                performance = 'Below average'
            elif sum(submark) - sum(avmark) > 0:
                if sum(topmark) - sum(submark) < 0.1:
                    performance = 'Excellent'
                else:
                    performance = 'Above average'
            else:
                performance= 'Average'
    if disci > 3:
        disci = 'A'
    elif disci == 3:
        disci = 'B'
    else:
        disci = 'C'
    tw = ''
    fail = []
    warn = []
    for i in subject:
        if 'D' in i['grade']:
            i['state'] = 'warning'
            warn.append(i['sub'])
        elif 'E' in i['grade']:
            fail.append(i['sub'])
            i['state'] = 'danger'
        else:
            i['state'] = ''
        if len(fail) > 0 :
            anre = f'Student should definitely improve {",".join(fail)}'
        else:
            anre = 'Marks are fine , maintain the record'
        if len(warn) > 0 :
            anre += f' <br>Need to work on {",".join(warn)} it\'s border line marks only the level of testing may increase in coming exams and the subjects won\'t come in hand'

        tem = Template('''<tbody>
             <tr class='table-$state'>
               <th  scope="row">$subj</th>
               <td>$internalMArks</td>
                <td>$markof</td>
               <td>$sumMark</td>
               <td>$grade</td>
             </tr>
           </tbody>''')
        tw += tem.safe_substitute(subj=i['sub'], internalMArks=i['internal'][0], markof=i['mark'][0],
                                 sumMark=i["totmark"], grade=i['grade'], state=i['state'])

    if len(fail) >= 2:
        failset = 'The student is retained and retest is not possible'
    elif len(fail) == 1:
        failset = 'The student is retained and retest can be attended if informed by administration'
    else:
        failset = ''


    categories = s
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=list(topmark),
        theta=categories,
        fill='toself',
        name='Class Topper'
    ))
    fig.add_trace(go.Scatterpolar(
        r=list(submark),
        theta=categories,
        fill='toself',
        name='Your Mark'
    ))
    fig.add_trace(go.Scatterpolar(
        r=list(avmark),
        theta=categories,
        fill='toself',
        name='Class average'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1]
            )),
        showlegend=False
    )

    fig.write_html("graph.html")
        # detail = [student_name , gr_number , Class , section , gaurdianName]
    html = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
      integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
      crossorigin="anonymous"
    />
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <style>
    .logo-img {
      max-width: 270px;
    }
    .details > * {
      margin-left: 10px;
    }
  </style>
  '''+f''''
  <body>
    <div class="d-flex justify-content-between pe-3 align-items-center">
      <img class="logo-img" src="logotext.png" />
      <div class="d-flex flex-column align-items-end">
        <span>PO Box:2324 Sharjah UAE </span
        ><span>Tel No:065665775 </span>boys@sissharjah.com<span
          >Fax:065672914</span
        >
        <span>Website: www.sisjuwaiza.com</span>
      </div>
    </div>
    <div class="text-center">
      <h1 class="display-3 fw-bolder">Report Card</h1>
    </div>
    <div class="d-flex">
      <div>
        <img src="logopic.png" alt="" style="width: 200px" />
      </div>
      <div class="p-5 fs-3 details">
        <span><strong>Name</strong>: {student_name}</span>
        <br />
        <span><strong>Gr. Number </strong>: {gr_number}</span>
        <span><strong> Guardian’s Name </strong>: {gaurdianName}</span>
        <br />
        <span><strong> Grade</strong>: {Class}</span>
        <span><strong> Section</strong>: {section}</span>
        <span><strong> Shift </strong>: A</span>
      </div>
    </div>
    <div class="p-5">
      <table class="table table-striped table-bordered border-dark">
        <thead>
          <tr>
            <th scope="col">Subjects</th>
          <th scope="col">Internals ({itrnl.split('/')[1]})</th>
            <th scope="col">Exam Mark ({temp.split('/')[1]})</th>
            <th scope="col">Total performance (100)</th>
            <th scope="col">Grade</th>
          </tr>
        </thead>
        {tw}
      </table>
       <div class="d-flex justify-content-between" style="margin-top: 100px">
        <span class="fs-3 fw-bold">Signature of Teacher</span>
        <span class="fs-3 fw-bold">Signature of Parent</span>
      </div>
    </div>
     <div class="d-flex px-5 flex-column">
      <h1 class="fw-bolder">Personal Remarks</h1>
      <span class="fs-5 fw-bolder"
        >Comparative performance:<span class="fw-light ms-2"
          >{performance}</span
        ></span
      >
      <span class="fs-5 fw-bolder"
        >Disciplinary:<span class="fw-light ms-2">{disci}</span></span
      >
      <span class="fs-5 fw-bolder"
        >Analytical Remarks:<span class="fw-light ms-2"><br>{anre}</span></span
      >
      <span class="fs-5 fw-bolder"
        >Personal Remarks:<br /><span class="fw-light ms-2">{remarks}</span></span
      >
            <span class="fs-5 fw-bolder text-danger "><br>{failset}</span>

    </div>
    <iframe
      src="graph.html"
      width="100%"
      height="600"
      frameborder="0"
    ></iframe>
  </body>
</html>
<script
  src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js"
  integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+"
  crossorigin="anonymous"
></script>'''
    print(subject)
    f = open(f"{gr_number}.html", "w")
    f.write(html)
    f.close()
    break




