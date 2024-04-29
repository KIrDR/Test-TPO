using Aircompany.Models;

namespace Aircompany.Planes
{
    public class MilitaryPlane : Plane
    {
        public MilitaryType planeType;

        public MilitaryPlane(string model, int maxSpeed, int maxFlightDistance, int maxLoadCapacity, MilitaryType type)
            : base(model, maxSpeed, maxFlightDistance, maxLoadCapacity)
        {
            planeType = type;
        }

        public override bool Equals(object obj)
        {
            return obj is MilitaryPlane plane &&
                   base.Equals(obj) &&
                   planeType == plane.planeType;
        }

        public override int GetHashCode()
        {
            int hashCode = base.GetHashCode();
            hashCode = hashCode * -1521134295 + planeType.GetHashCode();
            return hashCode;
        }

        public MilitaryType GetPlaneType()
        {
            return planeType;
        }

        public override string ToString()
        {
            return $"{base.ToString().TrimEnd('}')}, type={planeType}}}";
        }
    }
}
