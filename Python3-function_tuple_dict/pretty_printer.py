import pprint
pp = pprint.PrettyPrinter(indent=4)

mahasiswa = [
    {
        'nim' : '08/123123/PA/123213',
        'nama' : 'Guntur Budi H',
        'nilai' : [80,90,75,30]
    },
    {
        'nim' : '08/213123/PA/98120',
        'nama' : 'Annisa Maulida N',
        'nilai' : [100,90,77,110]
    }
]
mahasiswa_baru = {
    'nim' : '12/12414/PA/12312',
    'nama' : 'Miftahhurahma Rosyda'
}

mahasiswa.append(mahasiswa_baru)
mahasiswa[0]['nilai'].append(79)
mahasiswa[2]['nilai'] = [80,100,95,25]

#pp.pprint(mahasiswa)
pp.pprint(mahasiswa[0]['nilai'][-1])