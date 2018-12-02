x = linspace(1,20,20);

yGiniBest = yGiniBest();
yGiniRandom = yGiniRandom();
yEntropyBest = yEntropyBest();
yEntropyRandom = yEntropyRandom();
yAdaBoostedGiniBest = yAdaBoostedGiniBest();
yAdaBoostedGiniRandom = yAdaBoostedGiniRandom();
yAdaBoostedEntropyBest = yAdaBoostedEntropyBest();
yAdaBoostedEntropyRandom = yAdaBoostedEntropyRandom();

%% figure 1
figure(1);
plot(x, yGiniBest, 'r');
hold on;

plot(x, yGiniRandom, 'b');
hold off;

title('Probability For Successful Assignment Depending On Recursion Depth And Splitter')

legend({'Gini', 'Gini Random'},'Location','southeast')

xlabel('Recursion depth');
ylabel('Probability for successful assignment');

%% figure 2
figure(2);
plot(x, yEntropyBest, 'r');
hold on;

plot(x, yEntropyRandom, 'b');
hold off;

title('Probability For Successful Assignment Depending On Recursion Depth And Splitter')

legend({'Entropy best', 'Entropy Random'},'Location','southeast')

xlabel('Recursion depth');
ylabel('Probability for successful assignment');

%% figure 3
figure(3);
plot(x, yAdaBoostedEntropyBest, 'r');
hold on;

plot(x, yAdaBoostedEntropyRandom, 'b');
hold off;

title('Probability For Successful Assignment Depending On Recursion Depth And Splitter')

legend({'Entropy + AdaBoosted best', 'Entropy + AdaBoosted random'},'Location','southeast')

xlabel('Recursion depth');
ylabel('Probability for successful assignment');

%% figure 4
figure(4);
plot(x, yAdaBoostedGiniBest, 'r');
hold on;

plot(x, yAdaBoostedGiniRandom, 'b');
hold off;

title('Probability For Successful Assignment Depending On Recursion Depth And Splitter')

legend({'Gini + AdaBoosted best', 'Gini + AdaBoosted random'},'Location','southeast')

xlabel('Recursion depth');
ylabel('Probability for successful assignment');

