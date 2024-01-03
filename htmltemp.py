subject = [{'sub': 'physics', 'mark': ['18', '25'], 'internal': ['10', '10'], 'classav': ['12', '25'], 'classtop': ['24', '25'], 'grade': 'B1'}, {'sub': 'maths', 'mark': ['19', '25'], 'internal': ['10', '10'], 'classav': ['14', '25'], 'classtop': ['25', '25'], 'grade': 'B1'}, {'sub': 'chemistry', 'mark': ['15', '25'], 'internal': ['10', '10'], 'classav': ['13', '25'], 'classtop': ['19', '25'], 'grade': 'C1'}]



from string import Template

for i in subject:
    if 'D' in i['grade'] :
        i['state'] = 'warning'
    elif 'E' in i['grade']:
        i['state'] = 'danger'
    else:
        i['state'] = ''
    tem = Template('''<tbody>
         <tr class='table-$state'>
           <th  scope="row">$subj</th>
           <td>$internalMArks</td>
            <td>$markof</td>
           <td>$sumMark</td>
           <td>$grade</td>
         </tr>
       </tbody>''')
    tw = tem.safe_substitute(subj=i['sub'], internalMArks=i['internal'][0], markof=i['mark'][0], sumMark=i["totmark"], grade=i['grade'] , state = i['state'])
    print(tw)
