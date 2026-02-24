Python Slicing Direction Cheat Code

Condition	                        Direction	      Result	        Example	            Output

start < stop & step positive	  left → right	  ✅ Works	  "DataScience"[2:7]	      'taSci'
start > stop & step negative	  right → left	  ✅ Works	  "DataScience"[8:3:-1]	    'neicS'
start > stop & step positive	  left → right	  ❌ ''   	  "DataScience"[7:2]	        ''
start < stop & step negative	  right → left	  ❌ ''	      "DataScience"[2:8:-1]	      ''
------------------------------------------------------------------------------------

(Important)

1️⃣ Default step is +1
"DataScience"[2:5]

➡ moves left → right
------------------------------------------------------------------------------------

2️⃣ Negative step reverses direction
"DataScience"[::-1]

➡ full reverse
Output: 'ecneicSataD'
------------------------------------------------------------------------------------

3️⃣ Negative index ≠ reverse

It only changes starting position.

"DataScience"[-4:]

➡ 'ence'
Still moves left → right
------------------------------------------------------------------------------------

---------------
Mental Formula
---------------

Slicing = Walk from start toward stop using step.

If your walking direction and stop location don't match
You get '' (Empty Strings)



