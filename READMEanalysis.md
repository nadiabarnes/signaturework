# FIRST Robotics Alliance Selection Analyzer

## Background
FIRST robotics is a competition where a team of students build a robot, and robots are paired together and compete to get the most points in the time limit.
If you end in the top eight robots, you can choose any two robots to be on your team in finals instead of random pairings. It is important to select carefully.
This program is designed to assist in selecting the best robot for an alliance during a FIRST Robotics Competition. Using data collected from matches, the program calculates performance metrics and ranks teams based on customizable weightings. 
I all four years of high school in robotics, and this program was written freshman year of college when I was mentoring my old team.

---

## Features

### Data Processing
- **`readCsv()`**: Reads match data from a CSV file and organizes it into a list of dictionaries, where each dictionary represents a single match.

### Performance Metrics
1. **Match Participation**:
   - **`NumOfMatches()`**: Counts the number of matches recorded for each team.

2. **Teleoperated (Teleop) Performance**:
   - **`averageTele()`**: Calculates the average number of teleop shots taken per match for each team.
   - **`teleAccuracy()`**: Computes the percentage of successful teleop shots.

3. **Autonomous (Auto) Performance**:
   - **`maxAuto()`**: Finds the maximum number of successful autonomous shots for each team.
   - **`averageAuto()`**: Computes the average number of successful autonomous shots per match.

4. **Climbing Performance**:
   - **`maxClimb()`**: Determines the highest climbing level achieved by each team.
   - **`averageClimbPoints()`**: Calculates the average climbing points earned per match.

5. **Other Metrics**:
   - **`taxiLine()`**: Checks if a team consistently crosses the taxi line during matches.
   - **`averageIndPoints()`**: Calculates the average independent points scored by each team, considering auto, teleop, and climbing.

### Scoring and Ranking
- **`weighter()`**: Applies weights to each performance metric to calculate a weighted score out of 100 for each team.
- **`findMax()`**: Identifies the highest value in a given metric across all teams.

### Main Functionality
The `main()` function:
1. Prompts the user to input weightings for each performance metric.
2. Processes match data and calculates scores for each team.
3. Ranks teams based on their weighted scores.
4. Allows the user to display the top teams with either detailed or summarized performance data.

---

## File Requirements
The program reads data from a CSV file (`data5.csv`) that must include the following columns:
- `TEAM Number`
- `Total Teleop shots taken.`
- `Total Telop shots scored.`
- `Did they across the taxi line?`
- `How many successful autonomous shots?`
- `What level did they climb?`

---

## Usage

1. **Run the Program**:
   Execute the program, and it will guide you through inputting weights for the following metrics:
   - Average Teleop Score
   - Teleop Accuracy
   - Crossing the Taxi Line
   - Maximum Autonomous Shots
   - Average Autonomous Shots
   - Maximum Climb Level
   - Average Climb Points
   - Average Individual Points

2. **Input the Desired Output Length**:
   Specify the number of top-ranked teams to display.

3. **Choose Detail Level**:
   Select whether to display summarized scores or detailed performance statistics for each team.

---

## Example Output
- **Summarized**:
  ```
  1234 Score: 95.23
  5678 Score: 88.75
  ```

- **Detailed**:
  ```
  1234, Score: 95.23, Average Cargo Scored: 12.34,
  Teleop Accuracy: 87.5%, Taxi Line: yes,
  Average Auto Score: 5.67, Max Auto Score: 8,
  Max Climb: High, Average Climb Score: 7.89,
  Average Individual Points: 25.56
  ```

---

## Customization
The program allows you to:
- Adjust the weights for each performance metric.
- Control the number of teams displayed in the output.

---

