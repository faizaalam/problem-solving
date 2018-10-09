inputs = input().split();
inputs = list(map(int, inputs));

hour = inputs[1];
days = inputs[0];
hoursAm = hour;
hoursPm = hour + 12;
possible_hours = [];


for i in range(0,days):

    if i == 0:
        print(hoursAm);
        print(hoursPm); 
    
    if i > 0:
        print(hoursAm + (24* i));
        print(hoursPm + (24 * i)); 
		
		
Mr. Manchester Sy has a clock, which is of course labelled with the numbers . It is quite a strange clock, since it only has an hour hand, it doesn't have a minute hand or seconds hand.

Now, he has been playing Hearthstone on his computer for a very long time. He doesn't know how many hours exactly, but he is sure that he didn't play for more than  days, and that he started playing at exactly midnight.

Right now, the hour hand of the clock is pointing at . Can you tell him all the possible positive integer amounts of hours that he has been playing?

Origin:
ProgVar 2014 Session 3 Level 1

Input Format

The first and only line of input contains two integers   and  , which are the maximum number of days Mr. Sy has been playing and what the hour hand is pointing at right now.

Output Format

Output all the possible number of hours that Mr. Sy has been playing in ascending order, one in each line.

Sample Input

2 7
Sample Output

7
19
31
43
Explanation

In the sample test case, Mr. Manchester Sy has been playing for not more than two days, and currently, the hour hand is at .

It's possible he played for , ,  or  hours.

It's not possible that he played for more than that, because that would exceed two days.
    
    
    