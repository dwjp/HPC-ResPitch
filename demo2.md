## Demo 2 - Sudoku

Today we're going cheat at solving a sudoku puzzle using a supercomputer, and a technique called linear programming (https://en.wikipedia.org/wiki/Linear_programming). This is widely used optimization technique, used in everything from logistics to radiotherapy. None of that today though, we're using it for Sudoku! Below is the puzzle we're solving, details on how this is formulated are described [here](https://pythonhosted.org/PuLP/CaseStudies/a_sudoku_problem.html) for those interested.
 
 ![](wikisudokuproblem.jpeg)

This is a contrived example, but linear programming is a definite supercomputer application. The problem we're solving today will only take a fraction of a second, but often we need to scale to thousands or millions of parameters, which would take a very long time on a desktop computer.

1. First off, someone from your group will need an account on Spartan, our local supercomputer at The University of Melbourne. If you don't have one, let me know and I can invite you along to the demo project I've created for ResBaz. Follow the email instructions to setup a username and password.

2. Once your account has been created, you need to login via SSH. This gives you access to a command line prompt on Spartan which you can use to issue commands. The address you'll need is spartan.hpc.unimelb.edu.au, and the username/password you set in step 1. There are many different SSH clients available. If you're using Linux or OS X, it's already built in, just open a terminal window and type `ssh spartan.hpc.unimelb.edu.au`. If you're using Windows, you'll have to install a client. If you're using Chrome, you can try this [addon](https://chrome.google.com/webstore/detail/secure-shell/pnhechapfaindjhompbnflcldabbghjo). Another common option is [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html). Take care with your password; if you enter the wrong password too many times, you'll be locked out for a while!

3. To use a supercomputer, you need to know a little bit about Linux. But don't be scared! We'll run through this in the training, but you only need to know the basics to be productive. Let's start by typing the `ls` command and hitting Enter. That will tell us what's stored in our current directory (when you first login, this will be your home directory where you can store your files).

4. We're all working on a shared project I've created just for ResBaz. You can use this space to share files with your colleagues while you're working on them with Spartan. Type `cd /data/projects/punim0180`, which is the project I've created. If you get a permission denied error, you're not yet a member of that project; let me know and I'll add you!

5. Go into the sudoku subfolder with `cd sudoko`. In here is the Python program we want to run, and a job script that tells the supercomputer how to run it. If you type `less sudoku.slurm` you can view the contents of the job script.

6. Now let's submit the job, just type `sbatch sudoku.slurm`. Take note of the job number you're given.

7. Type `squeue -j <job number>`, using the number you were given above. Chances are our little job is already finished and so the list is empty, but most real jobs will some time, and we can use this to check how they're going.

8. If you give the `ls` command again, you should notice a new file called `slurm-<job number>.out`, again using the job number from above. Take a look at it with `less slurm-<job number>.out` -- it will give the output generated by your program, and tell you where to look for your Sudoku solution. Shout out if you get stuck!

9. Congratulations, you've run your first supercomputer job!
 
 

# Bonus Task

Find another Sudoku problem from the web, and modify the Python file `sudoku.py` to solve it.


