user = [
{
'nama': 'Arsene Lupin',
'nik': 1234,
'jenis_kelamin': 'Male',
'tanggal_lahir': '1902-03-23'
},
{
'nama': 'Sherlock Holmes',
'nik': 4321,
'jenis_kelamin': 'Male',
'tanggal_lahir': '1876-08-16'
},
{
'nama': 'Miss Marple',
'nik': 5678,
'jenis_kelamin': 'Female',
'tanggal_lahir': '1900-12-15'
}
]
def tambah_user(nama, nik, jenis_kelamin, tanggal_lahir):
user_baru = {
'nama': nama,
'nik': nik,
'jenis_kelamin': jenis_kelamin,
'tanggal_lahir': tanggal_lahir
}
user.append(user_baru)
return "Data user baru berhasil ditambahkan"