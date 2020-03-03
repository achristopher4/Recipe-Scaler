# Recipe-Scaler

Problem Description

Many recipes tend to be rather small, producing the fewest number of servings that are really possible with the included ingredients.   Sometimes one will want to be able to scale those recipes upwards for serving larger groups.

This program's task is to determine how much of each ingredient in a recipe will be required for a target party size.   The first inputs to the program will be the recipe itself.

Extra Credit Option

No doubt the output seems to be a little strange to ask for 2/4 pounds of butter.   One might think it would be better to ask for 1/2.

Modify the program so that all fractions are reduced to their lowest terms.  There is a function in the Python math library named gcd that can help with this.  Section 2.5 in the on-line text shows how to obtain that.

Also, express all improper fractions (where the numerator exceeds the denominator) as mixed fractions.   Scaling this recipe by a factor of 10 would ask for 2 1/2 pounds of butter.

And of course, the resulting output should still be easy to read.

ther Guidelines

Clarity of code is still important here -- and clear code is less likely to have bugs.

In particular, there should be very good and clear decisions in the code.

And there will be a penalty for usage of break or continue statements.

Planning out the design of the solution before diving into code will help!

The simplest solutions would use a list, but without any indexing on that list
(or use of range() to get those indexes).  Let Python help you fill and traverse the recipe.

Storing the entire recipe in a single list before splitting things up often produces much simpler programs than trying to store everything into multiple separate lists!

IMPORTANT NOTE:  As above, the recipe is provided as input to the program -- it is not part of the program itself.   The program may not assume it knows what the ingredients are, or how many there are, or which ingredients have fractions and which ones do not.  It must work for any number of valid input lines.
