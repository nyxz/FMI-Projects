#include <iostream>
#include <string.h>
using namespace std;

class Trip
{
private:
    char* dest;
    char* descr;
    int km;
    double price;

public:
    Trip(char* dest_, char* descr_, int km_, int price_);
    Trip(Trip const &t);
    ~Trip();
    Trip& operator=(Trip const &t);
    void set_dest(char* dest_);
    char* get_dest() const;
    void set_descr(char* descr_);
    char* get_descr() const;
    void set_km(int km);
    int get_km() const;
    void set_price(double price);
    double get_price() const;
    virtual void print() const;
};

Trip::Trip(char* dest_ = "default", char* descr_ = "default", int km_ = 0, int price_ = 0)
{
    cout << "============ Call Trip constructor." << endl;
    set_dest(dest_);
    set_descr(descr_);
    set_km(km_);
    set_price(price_);
}

Trip::~Trip()
{
    cout << "============ Call Trip Destructor." << endl;
    delete [] dest;
    delete [] descr;
}

Trip::Trip(Trip const &t)
{
    cout << "============ Call Trip copy-constructor." << endl;
    set_dest(t.get_dest());
    set_descr(t.get_descr());
    set_km(t.get_km());
    set_price(t.get_price());
}

Trip& Trip::operator=(Trip const &t)
{
    cout << "============ Call Trip operator = ." << endl;
    if (this == &t) return *this;

    delete [] dest;
    delete [] descr;

    set_dest(t.get_dest());
    set_descr(t.get_descr());
    set_km(t.get_km());
    set_price(t.get_price());

    return *this;
}

void Trip::set_dest(char* dest_)
{
    dest = new char[strlen(dest_) + 1];
    strcpy(dest, dest_);
}

char* Trip::get_dest() const
{
    return dest;
}

void Trip::set_descr(char* descr_)
{
    descr = new char[strlen(descr_) + 1];
    strcpy(descr, descr_);
}

char* Trip::get_descr() const
{
    return descr;
}

void Trip::set_km(int km_)
{
    km = km_;
}

int Trip::get_km() const
{
    return km;
}

void Trip::set_price(double price_)
{
    price = price_;
}

double Trip::get_price() const
{
    return price;
}

void Trip::print() const
{
    cout << "------ Trip ------" << endl
        << "Destination: " << get_dest() << endl
        << "Description: " << get_descr() << endl
        << "Length: " << km << endl
        << "Price: " << price << endl;
}

class BusTrip : public Trip
{
private:
    char* provider;
public:
    BusTrip(char* dest_, char* descr_, int km_, int price_, char* provider_);
    ~BusTrip();
    BusTrip(BusTrip const &bt);
    BusTrip& operator=(BusTrip const &bt);
    void set_provider(char* provider);
    char* get_provider() const;
    void print() const;
};

BusTrip::BusTrip(char* dest_, char* descr_, int km_, int price_, char* provider_)
    : Trip(dest_, descr_, km_, price_)
{
    cout << "============ Calling BusTrip constructor." << endl; 
    set_provider(provider_);    
}

BusTrip::~BusTrip()
{
    cout << "============ Calling BusTrip destructor." << endl; 
    delete [] provider;
}

BusTrip::BusTrip(BusTrip const &bt) : Trip(bt)
{
    cout << "============ Calling BusTrip copy-constructor." << endl; 
    set_provider(bt.get_provider());
}

BusTrip& BusTrip::operator=(BusTrip const &bt)
{
    cout << "============ Calling BusTrip operator =." << endl; 
    if (this == &bt) return *this;
    Trip::operator=(bt);
    delete [] provider;
    set_provider(bt.get_provider());

    return *this;
}

void BusTrip::set_provider(char* provider_)
{
    provider = new char[strlen(provider_) + 1];
    strcpy(provider, provider_);
}

char* BusTrip::get_provider() const
{
    return provider;
}

void BusTrip::print() const
{
    cout << "------ Bus Trip ------" << endl
        << "Provider: " << get_provider() << endl;
}

class PlaneFlight : public Trip
{
private:
    char* code;
    bool is_valid_code(char* code);
public:
    PlaneFlight(char* dest_, char* descr_, int km_, int price_, char* code);
    ~PlaneFlight();
    PlaneFlight(PlaneFlight const &pf);
    PlaneFlight& operator=(PlaneFlight const &pf);
    void set_code(char* code);
    char* get_code() const;
    void print() const;
};

PlaneFlight::PlaneFlight(char* dest_, char* descr_, int km_, int price_, char* code_)
    : Trip(dest_, descr_, km_, price_)
{
    set_code(code_);
}

PlaneFlight::~PlaneFlight()
{
    delete [] code;
}

PlaneFlight::PlaneFlight(PlaneFlight const &pf) : Trip(pf)
{
    set_code(pf.get_code());
}

PlaneFlight& PlaneFlight::operator=(PlaneFlight const &pf)
{
    if (this == &pf) return *this;

    delete [] code;

    Trip::operator=(pf);
    set_code(pf.get_code());

    return *this;
}

void PlaneFlight::set_code(char* code_)
{
    if (!is_valid_code(code_))
    {
        return;
    }
    code = new char[strlen(code_) + 1];
    strcpy(code, code_);
}

char* PlaneFlight::get_code() const
{
    return code;
}

bool PlaneFlight::is_valid_code(char* code)
{
    // TODO validation that make sense
    return true;
}

void PlaneFlight::print() const
{
    cout << "------ Flight ------" << endl
        << "Code: " << get_code() << endl;
}

class Tour 
{

};


int main()
{
    /*
    cout << endl << "-------------------------------------- Test Trip" << endl;
    Trip* trip = new Trip("Paris", "Cool trip", 1000, 500.50);
    trip->print_trip();
    trip->~Trip();
    Trip next_trip = *trip;

    Trip t1("Paris", "Cool trip", 1000, 500.50), t2("London", "Cool trip", 1000, 500.50);
    t1.print_trip();
    t2.print_trip();
    t1 = t2;
    t1.print_trip();
    t2.print_trip();
    */
    Trip* trip = new Trip("Paris", "Cool trip", 1000, 500.50);
    trip->print();

    cout << endl << "-------------------------------------- Test BusTrip" << endl;
    Trip* busTrip_1 = new BusTrip("Paris", "Cool trip", 1000, 500.50, "Union Ivconi");
    busTrip_1->print();

    Trip* test = new BusTrip("Paris", "Cool trip", 1000, 500.50, "Union Ivconi");
    test->print(); 

    Trip* flight = new PlaneFlight("Paris", "Cool trip", 1000, 500.50, "BG1234");
    return 0;
}
