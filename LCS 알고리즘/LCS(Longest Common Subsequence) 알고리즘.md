##  LCS(Longest Common Subsequence) 알고리즘



1. ### 개요

    LCS란 Longest Common Subsequence의 약자로 최장 공통 부분 문자열이다. 우리가 알고 있는 substring과 비교하면 substring은 연속된 부분 문자열이고 subsequence는 연속적이지는 않은 부분 문자열이다.

    예로 들어 Iamhungry라는 문자열에서 연속된 부분 문자열인 mhun은 substring이 되고 연속적으로 이어지지는 않았지만 순서는 맞는 mugy는 subsequence가 된다.

   ![img](https://t1.daumcdn.net/cfile/tistory/2129E647578398D221)

    그러면 LCS는 어디에 쓰일까? 대표적으로 LCS가 쓰이는 곳은 염기서열 유사성 분석이다. 이외에도 음파 단어 검색 및 교정 등에 사용된다.


2. ### 접근방법(1)- LCS의 길이 구하기

    DP(Dynamic Programming)으로 특정 범위까지의 값을 구하고 다른 범위까지의 값을 구할때 이전에 구해 둔 값을 이용하여 효율적으로 문제를 해결한다.



    LCS는 2개의 String을 비교하여 최장 공통 부분 문자열을 구해야한다. substring을 구하는 것과 다르게 연속적이지 않아도 되기 때문에 같은 길이의 다른 해가 나타날 수 있다.



   예시를 가지고 생각해 보자. 문자열 'ACAYKP'와 'CAPCAK'가 있다고 가정해보자.

   우선 하나의 String을 기준 String, 다른 String을 비교 String으로 둔다. 

   ![img](https://t1.daumcdn.net/cfile/tistory/211E5A4857839E6508)

    위 표를 보면 문자열 맨 앞에 0을 추가해 첫번째 행과 열이 모두 0이다. 두번째 열인 C열의 값을 집어 넣어 보자. 각 위치의 값은 LSC의 길이의 값이 들어간다.  

   ![img](https://t1.daumcdn.net/cfile/tistory/2652C94E57839C9420)

    값을 다 집어 넣으면 위 표와 같이 된다. 표를 읽는 법을 다시 설명하면 [C,C]의 1은 'C'와 'AC' 사이의 LCS의 길이이다. 마찬가지로 [C,Y]의 1은 'C'와 'ACAY'의 LCS의 길이를 나타낸 것이다.



    몇 번더 반복해 보자 

   ![img](https://t1.daumcdn.net/cfile/tistory/253B264B5783A0761D)

   ![img](https://t1.daumcdn.net/cfile/tistory/261BEC4B5783A07723)

    위 두표를 보면 알 수 있듯이 가로줄, **즉 행은 이전 행의 값을 기반으로 해서 계산된다.** 위의 두 표 중 1번째 표는 'CA'와 'ACAYKP'의 subsequence를 구한것이고, 2번째 표는 'CAP'와 'ACAYKP'의 subsequence를 구한 것이다.



    우리는 여기에서 표의 값을 구할 때 **같은 문자가 나오면** 이전까지의 LCS의 길이에 +1을 하는 것을 알 수 있다. 여기에서 이전까지의 LCS의 길이란 왼쪽값이 아니라 대각선(왼쪽 위)값을 말한다. 이는 두 문자열에서 해당 두 문자를 비교하기 전의 LCS의 길이에 +1을 하기 위해서 이다.



    또한 **비교한 문자가 다르다면**, 비교한 문자가 포함되어 있는 직전 LCS, 즉 표에서는 위와 왼쪽 값중 큰 값이 오게된다. 예를 들면 위의 2번째 표에서 [P,Y]의 값은 'CAP'와 'ACAY'를 비교한 값이 오게 되고, 'P'와 'Y'는 다르기 때문에 'CA'와 'ACAY'의 LCS의 길이와 'CAP'와 'ACA'의 LCS의 길이중 큰 값이 오게된다. 



    **즉 표의 값을 구하는 규칙은 다음과 같다.**

   1. String1[n], String2[k]가 같다면 : [n, k] == [n-1, k-1] + 1

   2. String1[n], String2[k]가 다르면 : [n, k] == [n-1, k]와 [n, k-1] 중 큰 값



3. ### 접근방법(2) - LCS 구하기

    문자열 'ACAYKP'와 'CAPCAK'를 이용해서 작성한 Table은 다음과 같다. 

   ![img](https://t1.daumcdn.net/cfile/tistory/26149A4F5783A8F90B)

    우선 가장 큰 숫자가 시작 된 곳을 체크한다. 이후 이전 숫자를 찾아 가며 체크를 하되, 각각의 행과 열에는 하나의 체크만이 있어야 한다.또한 앞서 말했듯이 substring을 구하는 것과 다르게 연속적이지 않아도 되기 때문에 같은 길이의 다른 해가 나타날 수 있다.

   ![img](https://t1.daumcdn.net/cfile/tistory/225D684B5783AAC90B)

   문자열 'ACAYKP'와 'CAPCAK'의 LCS는 'ACAK'이다.



출처: 

https://twinw.tistory.com/126

 [흰고래의꿈]
