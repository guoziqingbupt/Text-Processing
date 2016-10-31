import tf_idf


result = tf_idf.weightGen("Harry-Potter")

for key in result:
    print(key)
    for item in sorted(result[key].items()):
        print(item)
    print("***************************************")