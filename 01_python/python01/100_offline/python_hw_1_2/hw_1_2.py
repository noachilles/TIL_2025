# password는 제공된 스켈레톤 코드를 참조한다.
# 총 5개의 글자를 password 문장에서 찾아서 각각의 변수에 할당하여야 한다.
# first_char 변수에 할당할 글자는 password 문자열의 28번째부터 35번째까지에 작성된 글자이다.
# second_word 변수에 할당할 단어는 password 문자열의 113번째부터 총 5글자이다.
# third_word 변수에 할당할 단어는 password 문자열의 66번째부터 68번째까지 작성된 글자를 뒤집어서 출력한다.
# fourth_word 변수에 할당할 단어는 password 문자열의 322번째부터 총 4글자를 뒤집어서 출력한다.
# fifth_word 변수에 할당할 단어는 password 문자열의 365번째부터 작성된 python이다.
# 각 변수에 할당한 문자열을 f-string을 활용하여 출력하시오.

password = "In the bustling city, where life is a constant race against time, uoy often find yourself wondering if there's a shortcut to success. The vibrant lights of the cityscape illuminate the night, casting shadows on the short-lived dreams of those who seek fortune. As you navigate through the crowded streets, you realize the deen for guidance, like a compass pointing python. You need direction in this chaotic journey called life."

# 아래에 코드를 작성하시오.

first_char = password[28:35]
second_word = password[113:113+5]
third_word = password[68:65:-1]  
fourth_word = password[325:321:-1] # 321부터 325까지
fifth_word = password[365:365+len('python')]

print(f'{first_char} {second_word} {third_word} {fourth_word} "{fifth_word}".')