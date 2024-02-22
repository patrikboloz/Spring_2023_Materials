#include "car_dealership.h"


int main()
{
	Car_Dealership SantaFe;
	SantaFe.car_availability();
	SantaFe.current_stock();
	SantaFe.new_day();
	cout << SantaFe.user_choice(0,0) << endl;;

	return 0;
}