
///////////////////////////////////////////////////////////////////////////////////////////////////
/*

School Project for advanced C++ class.
- Simulate a bank teller lobby.  Have randomly generated customers arrive and wait in line.  Each
customer has a set of randomly generated characterstics (transaction type, dollar value, etc).
Depending on how many customers are in line the number of tellers will be adjusted.  Reports are
generated listing stats for customers at the end of the simulation.

by David Lang on 2019-11-03

*/
///////////////////////////////////////////////////////////////////////////////////////////////////

#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <sstream>
#include <iomanip>
#include <ctime>
#include <windows.h>

using namespace std;

// Assigns milliseconds between each main() while-loop step.
const int SLEEP_STEP = 250;
// Assigns probability of customer generation per minute (probability of 1 in 'CUSTOMER_CHANCE').
const int CUSTOMER_CHANCE = 6;
// Assigns maximum value that 'dollar' value can be per customer generation.
const int DOLLAR_MAX = 999;
// Assigns minimum value that 'trans_time' value can be per customer generation.
const int TRANS_TIME_MIN = 3;
// Assigns maximum value that 'trans_time' value can be per customer generation.
const int TRANS_TIME_MAX = 20;

const int LEN_TIMES = 240;
const string TIMES[LEN_TIMES] = {
  "10:00a", "10:01a", "10:02a", "10:03a", "10:04a", "10:05a", "10:06a", "10:07a", "10:08a",
  "10:09a", "10:10a", "10:11a", "10:12a", "10:13a", "10:14a", "10:15a", "10:16a", "10:17a",
  "10:18a", "10:19a", "10:20a", "10:21a", "10:22a", "10:23a", "10:24a", "10:25a", "10:26a",
  "10:27a", "10:28a", "10:29a", "10:30a", "10:31a", "10:32a", "10:33a", "10:34a", "10:35a",
  "10:36a", "10:37a", "10:38a", "10:39a", "10:40a", "10:41a", "10:42a", "10:43a", "10:44a",
  "10:45a", "10:46a", "10:47a", "10:48a", "10:49a", "10:50a", "10:51a", "10:52a", "10:53a",
  "10:54a", "10:55a", "10:56a", "10:57a", "10:58a", "10:59a",
  "11:00a", "11:01a", "11:02a", "11:03a", "11:04a", "11:05a", "11:06a", "11:07a", "11:08a",
  "11:09a", "11:10a", "11:11a", "11:12a", "11:13a", "11:14a", "11:15a", "11:16a", "11:17a",
  "11:18a", "11:19a", "11:20a", "11:21a", "11:22a", "11:23a", "11:24a", "11:25a", "11:26a",
  "11:27a", "11:28a", "11:29a", "11:30a", "11:31a", "11:32a", "11:33a", "11:34a", "11:35a",
  "11:36a", "11:37a", "11:38a", "11:39a", "11:40a", "11:41a", "11:42a", "11:43a", "11:44a",
  "11:45a", "11:46a", "11:47a", "11:48a", "11:49a", "11:50a", "11:51a", "11:52a", "11:53a",
  "11:54a", "11:55a", "11:56a", "11:57a", "11:58a", "11:59a",
  "12:00p", "12:01p", "12:02p", "12:03p", "12:04p", "12:05p", "12:06p", "12:07p", "12:08p",
  "12:09p", "12:10p", "12:11p", "12:12p", "12:13p", "12:14p", "12:15p", "12:16p", "12:17p",
  "12:18p", "12:19p", "12:20p", "12:21p", "12:22p", "12:23p", "12:24p", "12:25p", "12:26p",
  "12:27p", "12:28p", "12:29p", "12:30p", "12:31p", "12:32p", "12:33p", "12:34p", "12:35p",
  "12:36p", "12:37p", "12:38p", "12:39p", "12:40p", "12:41p", "12:42p", "12:43p", "12:44p",
  "12:45p", "12:46p", "12:47p", "12:48p", "12:49p", "12:50p", "12:51p", "12:52p", "12:53p",
  "12:54p", "12:55p", "12:56p", "12:57p", "12:58p", "12:59p",
  " 1:00p", " 1:01p", " 1:02p", " 1:03p", " 1:04p", " 1:05p", " 1:06p", " 1:07p", " 1:08p",
  " 1:09p", " 1:10p", " 1:11p", " 1:12p", " 1:13p", " 1:14p", " 1:15p", " 1:16p", " 1:17p",
  " 1:18p", " 1:19p", " 1:20p", " 1:21p", " 1:22p", " 1:23p", " 1:24p", " 1:25p", " 1:26p",
  " 1:27p", " 1:28p", " 1:29p", " 1:30p", " 1:31p", " 1:32p", " 1:33p", " 1:34p", " 1:35p",
  " 1:36p", " 1:37p", " 1:38p", " 1:39p", " 1:40p", " 1:41p", " 1:42p", " 1:43p", " 1:44p",
  " 1:45p", " 1:46p", " 1:47p", " 1:48p", " 1:49p", " 1:50p", " 1:51p", " 1:52p", " 1:53p",
  " 1:54p", " 1:55p", " 1:56p", " 1:57p", " 1:58p", " 1:59p",
};

const int LEN_NAMES = 30;
const string NAMES[LEN_NAMES] = {
  "David", "Carl ", "Ben  ", "Wendy", "Sarah", "Billy", "Sally", "Carla", "Susan", "Estel", "Gwen ",
  "Nancy", "Howey", "Brett", "Will ", "Bob  ", "Stan ", "Fred ", "Sam  ", "Owen ", "Maris", "Deb  ",
  "Neo  ", "Cloud", "Wilma", "Tifa ", "Gary ", "Tron ", "Alien", "Ghost"
};

const int LEN_TRANS_TYPES = 4;
const string TRANS_TYPES[LEN_TRANS_TYPES] = {
  "open      ", "close     ", "deposit   ", "withdrawal"
};





string generateCustomer(int _id, int _arrival_time) {
  /*
  Create the data storing string 'customer'.  Holds data pertaining to:
    - id            = Unique identifier.
    - name          = Randomly selected name from const 'NAMES'.
    - trans_type    = Randomly selected transaction type from const 'TRANS_TYPES'.
    - dollar        = Randomly selected dollar value between 1 and 'DOLLAR_MAX'.
    - arrival_time  = Value representing minute 'customer' was generated.
    - trans_time    = Value representing the length of the transaction randomly selected between
                      'TRANS_TIME_MIN' and 'TRANS_TIME_MAX'.
  */

  string customer_;
  string id, name, trans_type, dollar, arrival_time, trans_time;
  int i_dollar, i_trans_time;
  stringstream ss;

  // Generate 'name'.
  name = NAMES[0 + rand() % LEN_NAMES];
  // Generate 'trans_type'.
  trans_type = TRANS_TYPES[0 + rand() % LEN_TRANS_TYPES];
  // Generate 'dollar'.
  i_dollar = 1 + rand() % DOLLAR_MAX;
  ss.clear(); ss.str(""); ss << setw(3) << setfill('0') << i_dollar; dollar = ss.str();
  // Generate 'trans_time'.
  i_trans_time = TRANS_TIME_MIN + rand() % (TRANS_TIME_MAX - TRANS_TIME_MIN + 1);
  ss.clear(); ss.str(""); ss << setw(2) << setfill('0') << i_trans_time; trans_time = ss.str();
  // Convert 'id'.
  ss.clear(); ss.str(""); ss << setw(3) << setfill('0') << _id; id = ss.str();
  // convert 'arrival_time'.
  ss.clear(); ss.str(""); ss << setw(3) << setfill('0') << _arrival_time; arrival_time = ss.str();

  customer_ = id+"."+name+"."+trans_type+"."+dollar+"."+arrival_time+"."+trans_time;

  return customer_;
}





void displayLobby(int _time, vector<string> _customers) {
  /*
  Pretty print of general lobby information.
  */

  stringstream ss;
  string print_line_ = " +--------------+----------------------+";
  string time_ = " | time: " + TIMES[_time];
  string customers_count_; ss.clear(); ss.str(""); ss << _customers.size(); ss >> customers_count_;

  cout << print_line_ << endl;
  cout << time_ + " | total customers: " << setw(3) << customers_count_ << " |" << endl;
  cout << print_line_ << "\n" << endl;
}





void displayTellers(int _open[3], string _customer[3], string _trans_time[3]) {
  /*
  Pretty print of tellers and their status.
  */

  string print_line_ = " +----------+--------+----------------+--------------------+";
  string service_[2] = {"closed", "open  "};
  stringstream ss;

  for (int i = 0; i < 3; i++) {
    cout << print_line_ << endl;
    cout << " | Teller " << i + 1;
    cout << " | " << service_[_open[i]];
    cout << " | helping: " << _customer[i];
    int i_remaining = stoi(_trans_time[i]);
    string s_remaining; ss.clear(); ss.str(""); ss << i_remaining; ss >> s_remaining;
    cout << " | time remaining: " << setw(2) << s_remaining << " |" << endl;
  }
  cout << print_line_ << "\n" << endl;
}





void displayLine(queue<string> _line) {
  /*
  Pretty print of 'customers' waiting in '_line'.
  */

  string line_list[6] = {"", "", "", "", "", ""};
  string pretense;

  int line_count = 1;
  while (!_line.empty()) {
    string in_line = _line.front().substr(4, 5); _line.pop();
    if      (line_count <= 5)  { line_list[0] += in_line + " < "; }
    else if (line_count <= 10) { line_list[1] += in_line + " < "; }
    else if (line_count <= 15) { line_list[2] += in_line + " < "; }
    else if (line_count <= 20) { line_list[3] += in_line + " < "; }
    else if (line_count <= 25) { line_list[4] += in_line + " < "; }
    else                       { line_list[5] += in_line + " < "; }
    line_count += 1;
  }
  for (int i = 0; i < 6; i++) {
    if (i != 0 && line_list[i] == "") { break; }
    if (i == 0) { pretense = "WAITING LINE ... [ "; }
    else        { pretense = "                 [ "; }
    if (line_list[i].size() != 0) {
      line_list[i] = pretense + line_list[i].erase(line_list[i].size() - 2) + "]";
    }
    else {
      line_list[i] = pretense + "]";
    }
    cout << line_list[i] << endl;
  }
}





void generateCustomersSorted(vector<string> _customers, string _sort_by) {
  /*
  input:  _customers = Accumulated list of customers.
          _sort_by = Designates the method to sort.
  output: Print out of sorted _'customers'.
  */

  int size = _customers.size();
  int order[size];
  string set[size];

  // Generate 'pos' and 'len' form '_sort_by'.
  int pos, len;
  if      (_sort_by == "name")         { pos = 4;  len = 5; }
  else if (_sort_by == "dollar")       { pos = 21; len = 3; }
  else if (_sort_by == "arrival_time") { pos = 25; len = 3; }

  // Using 'pos' and 'len', extract working 'set' from '_customers' for sorting.
  for (int i = 0; i < size; i++) { set[i] = _customers[i].substr(pos, len); }

  // Perform sort.  Generates 'order', an int array of sorted element positions.
  for (int order_i = 0; order_i < size; order_i++) {
    string current_s = ""; int current_i = 0;
    for (int set_i = 0; set_i < size; set_i++) {
      if (set[set_i] > current_s) { current_s = set[set_i]; current_i = set_i; }
    }
    set[current_i] = "";
    order[order_i] = current_i;
  }

  // Pretty print.
  string line;
  line = " +----+-------+------------------+--------------+--------------+------------------+";
  cout << line << endl;
  cout << " | #  | name  | transaction type | dollar value | arrival time | transaction time |";
  cout << endl;
  cout << line << endl;
  for (int i = size - 1; i >= 0; i--) {
    string id           = _customers[order[i]].substr(1,  2);
    string name         = _customers[order[i]].substr(4,  5);
    string trans_type   = _customers[order[i]].substr(10, 8);
    string dollar       = _customers[order[i]].substr(21, 3);
    string arrival_time = _customers[order[i]].substr(25, 3);
    string trans_time   = _customers[order[i]].substr(29, 2);
    cout << " | " << id;
    cout << " | " << name;
    cout << " | "; cout.width(16); cout << left << trans_type;
    cout << " | "; cout.width(12); cout << left << "$" + dollar + ".00";
    cout << " | "; cout.width(12); cout << left << TIMES[stoi(arrival_time)];
    cout << " | "; cout.width(16); cout << left << trans_time + " minutes";
    cout << " |" << endl;
  }
  cout << line << endl;
}





void generateAvgTransactionTime(vector<string> _customers) {
  /*
  input:  _customers = List of customers to derive each customer's wait time from.
  output: Print average transaction time per customer.
  */

  int size = _customers.size();

  int total_wait_time = 0;
  for (int i = 0; i < size; i++) { total_wait_time += stoi(_customers[i].substr(29, 2)); }
  int avg_wait_time = total_wait_time / size;

  cout << "AVERAGE TRANSACTION TIME PER CUSTOMER = " << avg_wait_time << " minutes\n\n";
}





void generateAvgCustomersInLine(int _waiting_counts[LEN_TIMES]) {
  /*

  */

  // Average customers waiting in line is only calculated past close of lobby (1:00p) if there are
  // still customers in line past close of lobby.  'break_point' calculates when the last customer
  // is out of line after 1:00p.
  int break_point = 180;
  for (int i = LEN_TIMES - 1; i > 180; i--) {
    if (_waiting_counts[i] != 0) { break_point = i; break; }
  }

  int total_in_line = 0;
  for (int i = 0; i <= break_point; i++) { total_in_line += _waiting_counts[i]; }
  int avg_in_line = total_in_line / break_point;

  cout << "AVERAGE CUSTOMERS IN LINE PER MINUTE = " << avg_in_line << " customers\n";
}





int main() {

  srand(time(0));

  string customer;
  string empty = "     ";
  vector<string> customers;
  queue<string> line;
  int tlr_open[3] = {1, 0, 0};
  string tlr_customer[3] = {empty, empty, empty};
  string tlr_trans_time[3] = {"0", "0", "0"};
  int customers_waiting_counts[LEN_TIMES] = {0};
  stringstream ss;

  int time = 0; int id = 0;
  while (time < LEN_TIMES) {

    // Generate customers up to 1:00p.
    if (time < 180) {
      int generate = 0 + rand() % CUSTOMER_CHANCE;
      if (generate == 0) {

        customer = generateCustomer(id, time);
        customers.push_back(customer); line.push(customer);

        // With 'customer' generation also check for size of line for opening tellers.
        if      (line.size() == 5) { tlr_open[1] = 1; }
        else if (line.size() == 9) { tlr_open[2] = 1; }

        id += 1;
      }
    }
    else {
      if (
        line.size() == 0         && tlr_customer[0] == empty &&
        tlr_customer[1] == empty && tlr_customer[2] == empty
      ) { break; }
    }

    // Teller controls.
    for (int i = 0; i < 3; i++) {

      // Transaction time tracker.
      if (tlr_trans_time[i] != "0") {
        int holder = stoi(tlr_trans_time[i]) - 1;
        ss.clear(); ss.str(""); ss << holder; ss >> tlr_trans_time[i];
      }
      else {
        tlr_customer[i] = empty;
        // With 'tlr_trans_time[i] == 0' also check for size of line for closing tellers.
        if      (i == 1 && line.size() <= 4) { tlr_open[i] = 0; }
        else if (i == 2 && line.size() <= 8) { tlr_open[i] = 0; }
      }

      // Move 'customer' from 'line' to an open teller if conditions ...
      if (tlr_open[i] == 1 && tlr_customer[i] == empty && line.size() != 0) {
        string moving_to_teller = line.front(); line.pop();
        tlr_customer[i] = moving_to_teller.substr(4, 5);
        tlr_trans_time[i] = moving_to_teller.substr(29, 2);
      }
    }

    // Print outs.
    displayLobby(time, customers);
    displayTellers(tlr_open, tlr_customer, tlr_trans_time);
    displayLine(line);
    cout << "\n\n\n" << endl;

    // Accumulator for averages report generation.
    customers_waiting_counts[time] = line.size();

    // While-loop controls.
    Sleep(SLEEP_STEP);
    time += 1;
  }

  // Various customer list generations.
  cout << "CUSTOMER LIST BY NAME ...\n";
  generateCustomersSorted(customers, "name");
  cout << "\nCUSTOMER LIST BY DOLLAR VALUE ...\n";
  generateCustomersSorted(customers, "dollar");
  cout << "\nCUSTOMER LIST BY ARRIVAL TIME ...\n";
  generateCustomersSorted(customers, "arrival_time");
  cout << endl;
  // Averages generations.
  generateAvgTransactionTime(customers);
  generateAvgCustomersInLine(customers_waiting_counts);

  return 0;
}
