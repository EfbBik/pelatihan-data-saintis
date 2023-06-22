'''
contoh penggunaan opertator aritmatika
'''
# penjumlahan
print('penjumlahan')
print(2+5)
print('-'*20)
# pengurangan
print('pengurangan')
print(2-4)
print('-'*20)
# perkalian
print('perkalian')
print(2*6)
print('-'*20)
#pembagian
print('pembagian') 
print(2/4)
print('-'*20)
# modulus/ sisa hasil bagi
print('modulu/sisa hasil bagi')
print(7%2)
print('-'*20)
# perpangkatan
print('perpangkatan')
print(4**2)
print('-'*20)
# pembagian dengan hasil pembulatan flooring
print('pembagian dengan hasil pembulatan flooring')
print(7//2)
print('-'*20)


'''operator assignment'''
# penjumlahan
print('penjumlahan')
x=10
x=x+5
print(x)
x=9
x+=3
print(x)
print('-'*20)
# pengurangan
print('pengurangan')
x=10
x=x-5
print(x)
x=9
x-=3
print(x)
print('-'*20)
# perkalian
print('perkalian')
x=10
x=x*5
print(x)
x=9
x*=3
print(x)
print('-'*20)
# pembagian
print('pembagian')
x=10
x=x/5
print(x)
x=9
x/=3
print(x)
print('-'*20)
#modulus 
print('modulus')
x=10
x=x%5
print(x)
x=9
x%=3
print(x)
print('-'*20)
# pembagian flooring
print('pembagian flooring')
x=10
x=x//5
print(x)
x=9
x//=3
print(x)
print('-'*20)
# perpangkatan
print('perpangkatan')
x=5
x=x**2
print(x)
x=4
x**=3
print(x)
print('-'*20)

'''operator pembanding'''
print(4==4)
print(3!=3)
print(5>5)
print(6<6)
print(5>=5)
print(5<=5)
print('-'*20)

'''operator logika'''
print(False and False)
print(False or True)
print(not False and not True)
print('-'*20)

'''operator member ship/keanggotaan'''
a=(1,3,5,7,9,11)
b=5
print(b in a)
print('-'*20)
a=(0,1,1,2,3,5,8)
b=4
print(b not in a)
print('-'*20)

'''variabel'''

string= 'aku tampan'
integer=14
Float=8.2
boolean= False
Complex=4j+3
print(string)
print(integer)
print(Float)
print(boolean)
print(Complex)
print('-'*20)

'''tipe data dan konversi tipe data'''
print(type(string))
print(type(integer))
print(type(Float))
print(type(boolean))
print(type(Complex))
print('-'*20)

'''konversi tipe data'''
# konversi data integer
print(int(Float))
print(int(boolean))
print('-'*20)

# konversi data float
print(float(integer))
print(float(boolean))
print('-'*20)

# konversi data string
print(str(integer))
print(str(Float))
print(str(boolean))
print('-'*20)

# konversi data bool
print(bool(integer))
print(bool(Float))
print('-'*20)

# konversi data Complex
print(complex(integer))
print(complex(Float))
print(complex(boolean))
print('-'*20)