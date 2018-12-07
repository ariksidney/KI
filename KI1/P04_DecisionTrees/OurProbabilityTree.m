%% Task 3
%% Get Data

yOUrTreeTrainData = yOurTreeTrainData();
yOurTreeTestData = yOurTreeTestData();

x = linspace(1,16,16);

%% figure
figure();
plot(x, yOUrTreeTrainData, 'r');
hold on;

plot(x, yOurTreeTestData, 'b');
hold on;

title('Probablility for successful assignment depending on the recursion depth')

legend({'Train Data','Test Data'},'Location','southeast')

xlabel('Recursion depth');
ylabel('Probability for successful assignment');


