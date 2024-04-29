using Aircompany.Models;
using Aircompany.Planes;
using System;
using System.Collections.Generic;
using System.Linq;

namespace Aircompany
{
    public class Airport
    {
        private List<Plane> planes;

        public Airport(IEnumerable<Plane> planes)
        {
            this.planes = planes.ToList();
        }

        public List<PassengerPlane> GetPassengerPlanes()
        {
            return planes.OfType<PassengerPlane>().ToList();
        }

        public List<MilitaryPlane> GetMilitaryPlanes()
        {
            return planes.OfType<MilitaryPlane>().ToList();
        }

        public PassengerPlane GetPassengerPlaneWithMaxPassengerCapacity()
        {
            return GetPassengerPlanes().Aggregate((w, x) => w.GetPassengersCapacity() > x.GetPassengersCapacity() ? w : x);

        }


        public List<MilitaryPlane> GetTransportMilitaryPlanes()
        {
            return GetMilitaryPlanes().Where(m => m.GetPlaneType() == MilitaryType.TRANSPORT).ToList();
        }

        public Airport SortByMaxDistance()
        {
            return new Airport(planes.OrderBy(p => p.MaxFlightDistance));
        }

        public Airport SortByMaxSpeed()
        {
            return new Airport(planes.OrderBy(p => p.MaxSpeed));
        }

        public Airport SortByMaxLoadCapacity()
        {
            return new Airport(planes.OrderBy(p => p.MaxLoadCapacity));
        }

        public IEnumerable<Plane> GetPlanes()
        {
            return planes;
        }

        public override string ToString()
        {
            return "Airport{" +
                    "planes=" + string.Join(", ", planes.Select(p => p.Model)) +
                    '}';
        }
    }
}
