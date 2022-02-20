export function getRandId(min: number = 1017, max: number = 1524): number {
  //The maximum is inclusive and the minimum is inclusive

  min = Math.ceil(min);
  max = Math.floor(max);

  return Math.floor(Math.random() * (max - min + 1) + min);
}

const host = "localhost";

export const apiUrl = `http://${host}:8000/znaci/pitanje/`;
export const apiSlikeUrl = `http://${host}:8000/static/srbija/`;
