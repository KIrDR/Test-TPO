﻿using System;

namespace Aircompany.Planes
{
    public class PassengerPlane : Plane
    {
        public int passengersCapacity;

        public PassengerPlane(string model, int maxSpeed, int maxFlightDistance, int maxLoadCapacity, int passengersCapacity)
            : base(model, maxSpeed, maxFlightDistance, maxLoadCapacity)
        {
            this.passengersCapacity = passengersCapacity;
        }

        public override bool Equals(object obj)
        {
            return obj is PassengerPlane plane &&
                   base.Equals(obj) &&
                   passengersCapacity == plane.passengersCapacity;
        }

        public override int GetHashCode()
        {
            int hashCode = base.GetHashCode();
            hashCode = hashCode * -1521134295 + passengersCapacity.GetHashCode();
            return hashCode;
        }

        public int GetPassengersCapacity()
        {
            return passengersCapacity;
        }

        public override string ToString()
        {
            return $"{base.ToString().TrimEnd('}')}, passengersCapacity={passengersCapacity}}}";
        }
    }
}
