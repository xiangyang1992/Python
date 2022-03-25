import pickle

data1 = {
    'a':[1,2.0,3,4+6j],
    'b':('string',u'Unicode string'),
    'c': None
}

selfref_list = [1,2,3]
selfref_list.append(selfref_list)

out_put = open('data.pkl','wb')
pickle.dump(data1,out_put)
pickle.dump(selfref_list,out_put,-1)

out_put.close()