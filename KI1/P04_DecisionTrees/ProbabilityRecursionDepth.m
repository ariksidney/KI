%% Get values
x = linspace(1,20,20);

yGini = yGiniBest();
yEntropy = yEntropyBest();
yAdaBoostedGini = yAdaBoostedGiniBest();
yAdaBoostedEntropy = yAdaBoostedEntropyBest();

%% figure
figure();
plot(x, yGini, 'r');
hold on;

plot(x, yEntropy, 'b');
hold on;

plot(x, yAdaBoostedGini, 'g');
hold on; 

plot(x, yAdaBoostedEntropy, '--c');
hold on;

title('Probablility for successful assignment depending on the recursion depth')

legend({'Gini','Entropy','Gini + AdaBoost','Entropy + AdaBoost'},'Location','southeast')

xlabel('Recursion depth');
ylabel('Probability for successful assignment');
