variable = 'this is bold'

print('this is NOT bold ' + '\033[1m' +
      variable + '\033[0m' + ' this is NOT bold')