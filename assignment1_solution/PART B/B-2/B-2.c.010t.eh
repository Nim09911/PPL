
;; Function main (main, funcdef_no=0, decl_uid=1969, cgraph_uid=0, symbol_order=1)

main ()
{
  int a;
  int i;
  int D.1977;

  a = 10;
  i = 0;
  goto <D.1974>;
  <D.1973>:
  N.0_1 = N;
  a = a + N.0_1;
  i = i + 1;
  <D.1974>:
  if (i <= 3) goto <D.1973>; else goto <D.1975>;
  <D.1975>:
  D.1977 = a;
  goto <D.1978>;
  D.1977 = 0;
  goto <D.1978>;
  <D.1978>:
  return D.1977;
}


