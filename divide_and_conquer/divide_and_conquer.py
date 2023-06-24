private static boolean estaEnPosicion(List<Integer> list)
	{
		return estaEnList(list, 0, list.size());
	}

	private static boolean estaEnList(List<Integer> list, int min, int max)
	{
		if (min>max){
			return false;
		}

		Integer newIndex = (min + max) / 2;

		if (list.get(newIndex) == newIndex)
		{
			return true;
		}

		if(list.get(newIndex)<newIndex){
			return estaEnList(list, min+1, max);
		}
		else{
			return estaEnList(list, min, newIndex-1);
		}

	}

	private static Boolean masALaIzq(List<Integer> list)
	{
		/*if(list.isEmpty())
		{
			return false;
		}*/

		if(list.size()==1)
		{
			return true;
		}

		if(list.size()==2)
		{
			return list.get(0)> list.get(1);
		}

		Integer pivote = list.size()/2;
		List<Integer> subListTi = list.subList(0, pivote);
		List<Integer> subListTd = list.subList(pivote, list.size());
		Integer sumaTi = subListTi.stream().mapToInt(Integer::intValue).sum();
		Integer sumaTd = subListTd.stream().mapToInt(Integer::intValue).sum();

		Boolean ti = masALaIzq(subListTi);
		Boolean td = masALaIzq(subListTd);

		return sumaTi > sumaTd && ti && td;

	}