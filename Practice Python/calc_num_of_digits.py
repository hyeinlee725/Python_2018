number=int(input("정수를 입력하시오: "))
print("자리수의 합: ",(number%10)+((number//10)%10)+((number//100)%10)+
      ((number//1000)%10))
