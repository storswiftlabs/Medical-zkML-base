program dt.aleo {
	struct Inputs {
		p1: u32,
		p2: u32,
		p3: u32,
		p4: u32,
		p5: u32,
		p6: u32,
		p7: u32,
		p8: u32,
		p9: u32,
		p10: u32,
		p11: u32,
		p12: u32,
		p13: u32,
	}
	// Code auto generated from DecisionTreeClassifier using dt_to_leo_code.py 
	transition main(inputs: Inputs) -> public u32 {
		if (inputs.p13 < 45u32) {
			if (inputs.p1 < 555u32) {
				if (inputs.p12 < 5u32) {
					if (inputs.p10 < 36u32) {
						return 0u32;
					} else {
						return 1u32;
					}
				} else {
					if (inputs.p4 <= 1210u32) {
						if (inputs.p5 < 2825u32) {
							if (inputs.p2 < 5u32) {
								return 0u32;
							} else {
								return 1u32;
							}
						} else {
							return 2u32;
						}
					} else {
						return 0u32;
					}
				}
			} else {
				if (inputs.p2 < 5u32) {
					if (inputs.p1 < 635u32) {
						if (inputs.p10 < 14u32) {
							if (inputs.p4 <= 1540u32) {
								if (inputs.p7 <= 10u32) {
									return 0u32;
								} else {
									if (inputs.p5 <= 3110u32) {
										if (inputs.p5 <= 2440u32) {
											return 1u32;
										} else {
											return 0u32;
										}
									} else {
										if (inputs.p8 < 1605u32) {
											return 3u32;
										} else {
											return 1u32;
										}
									}
								}
							} else {
								return 1u32;
							}
						} else {
							return 1u32;
						}
					} else {
						return 0u32;
					}
				} else {
					if (inputs.p12 < 5u32) {
						if (inputs.p5 <= 2720u32) {
							if (inputs.p10 < 24u32) {
								return 0u32;
							} else {
								return 1u32;
							}
						} else {
							if (inputs.p3 < 35u32) {
								return 1u32;
							} else {
								return 0u32;
							}
						}
					} else {
						if (inputs.p1 <= 600u32) {
							return 1u32;
						} else {
							if (inputs.p9 < 5u32) {
								if (inputs.p3 < 25u32) {
									return 0u32;
								} else {
									return 1u32;
								}
							} else {
								if (inputs.p11 < 25u32) {
									if (inputs.p10 < 1u32) {
										return 4u32;
									} else {
										if (inputs.p1 < 635u32) {
											return 4u32;
										} else {
											return 2u32;
										}
									}
								} else {
									return 3u32;
								}
							}
						}
					}
				}
			}
		} else {
			if (inputs.p12 < 5u32) {
				if (inputs.p9 < 5u32) {
					if (inputs.p1 <= 510u32) {
						if (inputs.p1 < 445u32) {
							if (inputs.p7 <= 10u32) {
								if (inputs.p10 < 11u32) {
									return 0u32;
								} else {
									return 3u32;
								}
							} else {
								return 1u32;
							}
						} else {
							if (inputs.p4 <= 1220u32) {
								return 1u32;
							} else {
								if (inputs.p1 <= 490u32) {
									return 3u32;
								} else {
									return 4u32;
								}
							}
						}
					} else {
						if (inputs.p4 <= 1510u32) {
							return 0u32;
						} else {
							if (inputs.p10 < 11u32) {
								if (inputs.p6 < 5u32) {
									return 1u32;
								} else {
									return 0u32;
								}
							} else {
								return 0u32;
							}
						}
					}
				} else {
					if (inputs.p5 < 2405u32) {
						if (inputs.p10 < 18u32) {
							if (inputs.p4 <= 1430u32) {
								return 0u32;
							} else {
								return 3u32;
							}
						} else {
							if (inputs.p13 < 65u32) {
								return 2u32;
							} else {
								return 3u32;
							}
						}
					} else {
						if (inputs.p11 < 25u32) {
							if (inputs.p1 <= 660u32) {
								if (inputs.p5 <= 3020u32) {
									return 1u32;
								} else {
									if (inputs.p1 <= 560u32) {
										return 2u32;
									} else {
										return 1u32;
									}
								}
							} else {
								return 3u32;
							}
						} else {
							return 2u32;
						}
					}
				}
			} else {
				if (inputs.p1 < 535u32) {
					if (inputs.p12 < 15u32) {
						if (inputs.p9 < 5u32) {
							return 1u32;
						} else {
							return 0u32;
						}
					} else {
						return 3u32;
					}
				} else {
					if (inputs.p5 <= 1800u32) {
						return 3u32;
					} else {
						if (inputs.p8 < 1125u32) {
							if (inputs.p3 < 35u32) {
								if (inputs.p10 < 14u32) {
									return 2u32;
								} else {
									return 3u32;
								}
							} else {
								return 1u32;
							}
						} else {
							if (inputs.p5 <= 2040u32) {
								return 2u32;
							} else {
								if (inputs.p11 < 15u32) {
									if (inputs.p4 < 1215u32) {
										if (inputs.p1 < 625u32) {
											return 2u32;
										} else {
											if (inputs.p8 < 1545u32) {
												return 0u32;
											} else {
												return 1u32;
											}
										}
									} else {
										if (inputs.p10 < 16u32) {
											return 1u32;
										} else {
											if (inputs.p12 < 15u32) {
												return 1u32;
											} else {
												return 3u32;
											}
										}
									}
								} else {
									if (inputs.p1 < 555u32) {
										if (inputs.p4 <= 1460u32) {
											return 3u32;
										} else {
											return 4u32;
										}
									} else {
										if (inputs.p4 <= 1740u32) {
											if (inputs.p5 <= 2350u32) {
												if (inputs.p6 < 5u32) {
													if (inputs.p4 <= 1290u32) {
														if (inputs.p4 <= 1160u32) {
															return 4u32;
														} else {
															return 1u32;
														}
													} else {
														if (inputs.p3 < 35u32) {
															return 0u32;
														} else {
															return 4u32;
														}
													}
												} else {
													return 2u32;
												}
											} else {
												if (inputs.p10 < 35u32) {
													if (inputs.p8 < 1535u32) {
														if (inputs.p4 < 1625u32) {
															if (inputs.p4 < 1275u32) {
																if (inputs.p1 < 595u32) {
																	return 2u32;
																} else {
																	return 1u32;
																}
															} else {
																return 2u32;
															}
														} else {
															return 4u32;
														}
													} else {
														if (inputs.p8 < 1665u32) {
															return 3u32;
														} else {
															return 2u32;
														}
													}
												} else {
													return 4u32;
												}
											}
										} else {
											return 3u32;
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
}