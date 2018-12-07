x = linspace(1,14,14);

yOurTreeTestData = yOurTreeTestData();
yEntropyBest = yEntropyBest();
yGiniBest = yGiniBest();
yAdaBoostedGiniBest = yAdaBoostedGiniBest();
yAdaBoostedEntropyBest = yAdaBoostedEntropyBest();

%% figure 1
figure(1);
plot(x, yOurTreeTestData(1:14), 'b');
hold on;

plot(x, yGiniBest(1:14), 'r');
hold on;

plot(x, yEntropyBest(1:14), 'y');
hold on;

plot(x, yAdaBoostedGiniBest(1:14), 'g');
hold on;

plot(x, yAdaBoostedEntropyBest(1:14), '--r');
hold on;

title('Probability For Successful Assignment Depending On Recursion Depth')

legend({'Our Tree', 'Gini', 'Entropy', 'AdaBoost + Gini', 'AdaBoost + Entropy'},'Location','southeast')

xlabel('Recursion depth');
ylabel('Probability for successful assignment');
