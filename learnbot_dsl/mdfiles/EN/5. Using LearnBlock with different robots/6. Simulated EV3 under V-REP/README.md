<a name="Init"></a>

# Simulated EV3 under V-REP

Using the simulated version of EV3 firstly requires for the installation of the V-REP simulator. You can get different versions of V-REP from [http://www.coppeliarobotics.com/](http://www.coppeliarobotics.com/) (V-REP PRO, recommended version: 3.6.2). In addition, you will need to install the packages *liblua5.1-0-dev* and *inputs* by typing the following commands:

	sudo apt install liblua5.1-0-dev

	sudo pip3 install inputs

Once you have installed V-REP, you will need to download the scene file including the EV3 robot (*ev3.ttt*). Such file can be downloaded using the following command: 

	wget https://raw.githubusercontent.com/robocomp/LearnBlock/version-3/LB_add_files/ev3.ttt

Start V-REP and open *ev3.ttt*. Once you start the simulation, you can run programs created with LearnBlock on the simulated EV3 (see the section [Program execution](<hidepath>/EN/4. Program execution/README.html)).
 
[Init^](#Init)

