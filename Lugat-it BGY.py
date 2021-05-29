import sys
while True:
    Secim = input("Hangi dilden dile çevirmek istiyorsunuz?\n Türkçe'den Lugat-it BGY için 1\n Lugat-it BGY'den Türkçe'ye için 0'a basınız\n")
    if Secim == '0':
        lugatta = input("Lugatça kelime:")
        lugattakucuk = lugatta.lower()
        cevirilmemistemp = lugattakucuk.replace('a', '%ta%').replace('b', '%tb%').replace('c', '%tc%').replace('ç', '%tç%').replace('d', '%td%').replace('e', '%te%').replace('f', '%tf%').replace('g', '%tg%').replace('ğ', '%tğ%').replace('h', '%th%').replace('i', '%ti%').replace('ı', '%tı%').replace('j', '%tj%').replace('k', '%tk%').replace('l', '%tl%').replace('m', '%tm%').replace('n', '%tn%').replace('o', '%to%').replace('ö', '%tö%').replace('p', '%tp%').replace('r', '%tr%').replace('s', '%ts%').replace('ş', '%tş%').replace('t', '%tt%').replace('u', '%tu%').replace('ü', '%tü%').replace('v', '%tv%').replace('y', '%ty%').replace('z', '%tz%')
        cevirilmis= cevirilmemistemp.replace('%%tt%e%', 'a').replace('%%tt%z%', 'b').replace('%%tt%v%', 'c').replace('%%tt%y%', 'ç').replace('%%tt%p%', 'd').replace('%%tt%a%', 'e').replace('%%tt%j%', 'f').replace('%%tt%k%', 'g').replace('%%tt%l%', 'ğ').replace('%%tt%r%', 'h').replace('%%tt%ö%', 'i').replace('%%tt%o%', 'ı').replace('%%tt%f%', 'j').replace('%%tt%g%', 'k').replace('%%tt%ğ%', 'l').replace('%%tt%c%', 'm').replace('%%tt%ç%', 'n').replace('%%tt%u%', 'o').replace('%%tt%ü%', 'ö').replace('%%tt%b%', 'p').replace('%%tt%d%', 'r').replace('%%tt%m%', 's').replace('%%tt%n%', 'ş').replace('%%tt%h%', 't').replace('%%tt%ı%', 'u').replace('%%tt%i%', 'ü').replace('%%tt%s%', 'v').replace('%%tt%ş%', 'y').replace('%%tt%t%', 'z')
        print("Türkçe : " + cevirilmis)
        sys.exit(" ")

    elif Secim == '1':
        lugatta = input("Türkçe kelime:")
        lugattakucuk = lugatta.lower()
        cevirilmemistemp = lugattakucuk.replace('a', '%ta%').replace('b', '%tb%').replace('c', '%tc%').replace('ç', '%tç%').replace('d', '%td%').replace('e', '%te%').replace('f', '%tf%').replace('g', '%tg%').replace('ğ', '%tğ%').replace('h', '%th%').replace('i', '%ti%').replace('ı', '%tı%').replace('j', '%tj%').replace('k', '%tk%').replace('l', '%tl%').replace('m', '%tm%').replace('n', '%tn%').replace('o', '%to%').replace('ö', '%tö%').replace('p', '%tp%').replace('r', '%tr%').replace('s', '%ts%').replace('ş', '%tş%').replace('t', '%tt%').replace('u', '%tu%').replace('ü', '%tü%').replace('v', '%tv%').replace('y', '%ty%').replace('z', '%tz%')
        cevirilmis= cevirilmemistemp.replace('%%tt%a%', 'e').replace('%%tt%b%', 'z').replace('%%tt%c%', 'v').replace('%%tt%ç%', 'y').replace('%%tt%d%', 'p').replace('%%tt%e%', 'a').replace('%%tt%f%', 'j').replace('%%tt%g%', 'k').replace('%%tt%ğ%', 'l').replace('%%tt%h%', 'r').replace('%%tt%i%', 'ö').replace('%%tt%ı%', 'o').replace('%%tt%j%', 'f').replace('%%tt%k%', 'g').replace('%%tt%l%', 'ğ').replace('%%tt%m%', 'c').replace('%%tt%n%', 'ç').replace('%%tt%o%', 'u').replace('%%tt%ö%', 'ü').replace('%%tt%p%', 'b').replace('%%tt%r%', 'd').replace('%%tt%s%', 'm').replace('%%tt%ş%', 'n').replace('%%tt%t%', 'h').replace('%%tt%u%', 'ı').replace('%%tt%ü%', 'i').replace('%%tt%v%', 's').replace('%%tt%y%', 'ş').replace('%%tt%z%', 't')
        print("Lugatça : " + cevirilmis)
        sys.exit(" ")
    else:
        print("Lütfen geçerli bir seçeneği tuşlayınız!")
        break