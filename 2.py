def func(bin):
    try:
        d = int(bin, 2)
        print(f"المكافئ العشري للرقم الثنائي {bin} هو {d}")
    except ValueError:
        print("تم إدخال رقم ثنائي غير صالح.")

s = input("أدخل رقم ثنائي")
func(s)
