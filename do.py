import json, sys


def out_json():
	open_file = open('t.json', 'r')
	data = open_file.read()
	out = json.loads(data)
	return out


def filte(ty, keyword, data):
	true_id = []
	if ((ty == 'No') or (ty == '分局') or (ty == '所別') or (ty == '里別') or (ty == '設置地點') or (ty == '監視器編號')):
		for i in range(1,23038):
			if keyword in data['result']['records'][i][ty]:
				true_id.append(i)
	else:
		pass
	return true_id


def show(_id, data):
	n = len(_id)
	if n != 0:
		print('\t%s \t%s \t\t%s' %('NO', '分局', '測照地點'))
		print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
		for i in range(n):
			num = _id[i]
			db = data['result']['records'][num]
			#print(num)
			print('\t%s \t%s \t%s' %(db['_id'], db['分局'], db['設置地點']))
			#print(data['result']['records'][num])
	else:
		print('無資料...')


if __name__ == '__main__':
	data = out_json()
	try:
		ty = sys.argv[1]
	except:
		ty = input("你想找的類型(No/分局/所別/里別/設置地點/監視器編號) ? << ")
	try:
		key = sys.argv[2]
	except:
		key = input("你想找'%s'的Keyword ? << " %ty)
	out_list = filte(ty, key, data)
	#out_list = [1, 2, 3]
	show(out_list, data)