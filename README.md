# A Monte Carlo simulation to predict how strong Franks’ Paladin is against other units in Age of Empires II  </br>
### Scenario:</br>
Age of Empires II (AoE II) is a real-time strategic game developed and published by Microsoft in 1999, and two remastered editions were released in 2013 (HD version) and 2019 (Definitive Edition). The game is still one of my favorite games after 21 years have passed and the 2-D art design is still amazing in modern days. Age of Empires II is still the most popular RTS game on PC in 2020.</br>
Franks was famous for cavalry combat in history. In this game, Paladins (heavy calvary) from Franks have 20% percent more health than other civilizations. However, the lack of Bloodlines technology makes them have the maximum of 192 health. Some civilizations like Spanish have 180 health for their Paladins and some only have 160 health.</br>
I’m trying to use Monte Carlo simulation to predict the win rate of a certain number of Paladins against other units in this game. For example, how many normal Paladins can 40 Franks Paladins counter and win the fight? What about Champion, Halberdier, Teutonic Knight?</br>
</br>
![alt text](https://static.wikia.nocookie.net/ageofempires/images/2/28/Paladin_aoe2DE.png/revision/latest/scale-to-width-down/256?cb=20200401180849)
### Hypothesis:
The 20% additional health will give Franks a moderate advantage in fights.
### Random variables:
1. The number of soldiers attacking the same unit simultaneously.
### Fixed rules:
1. All units are upgraded to their full potential. 
2. For simplicity, we assume all units are stuffed into a small arena and it takes no time to move and attack next target.
3. All units have the same attack rate.
4. All data are based on the Definitive Edition.
### Expected Results:
I will plot the simulated results of win rates so the user can view at which point Franks starts losing. I am considering adding the number of units lost and total health remain as part of results.

### Data sources:
https://en.wikipedia.org/wiki/Age_of_Empires_II </br>
https://ageofempires.fandom.com/wiki/Age_of_Empires_II:_Definitive_Edition

